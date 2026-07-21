# NLP2SQL 数据库查询图表工作流

## 1. 基本介绍

NLP2SQL（或称 Text2SQL）是一种自然语言处理技术，旨在将自然语言问题转化为关系型数据库中可执行的结构化查询语言（SQL），从而实现对数据库的查询和交互。核心目标是通过自然语言描述，无需用户具备 SQL 语法知识，即可完成复杂的数据库查询任务。

## 2. 工具安装

本次工作流用到了三个工具：**时间工具、ECharts 图表生成、Database 数据库插件**。

![工具安装概览](../../images/6.3/00.png)

- **注意：** 安装 Database 插件时，需要进行 API Key 的配置

![Database API Key 配置](../../images/6.3/001.png)

- **数据库 URI 配置格式：**

```properties
mysql+pymysql://root:123456@host.docker.internal:3306/dify_test
#                    ↑密码      ↑Docker内部地址      ↑数据库名
```

![数据库 URI 配置](../../images/6.3/002.png)

## 3. 整体流程

### 3.1 开始节点

![开始节点](../../images/6.3/01.png)

- **作用：** 用户输入，接受用户输出的问题
- 针对该节点默认输入即可，不用修改

### 3.2 大模型：生成 SQL 查询语句

![SQL生成大模型节点](../../images/6.3/03.png)

**作用：** 根据用户提出的问题，生成 SQL 查询语句

#### 配置节点内容

1. **模型选择：** `qwen3-max`

2. **系统提示词：**

```markdown
## 角色
你是一个专业的SQL查询生成器，负责根据用户查询创建标准的MySQL数据库SQL语句。

## 任务
根据以下问题，生成一个格式清晰、结构明确的JSON数组。

### 表信息
表名：student_grades（学生成绩信息表）

### 字段说明
- id: 主键
- student_id: 学号
- student_name: 学生姓名
- class_name: 班级
- subject: 科目
- score: 分数
- exam_date: 考试日期
- semester: 学期
- grade: 年级
- created_at: 记录创建时间
- updated_at: 记录更新时间

### 输出要求
1. 生成最多10条直接关联问题的SQL查询语句。
2. 每条SQL应从不同分析角度切入。
3. 所有SQL必须语法正确、可执行。
4. 最终输出必须是纯JSON数组格式。
```

3. **用户提示词示例：** 查询全校各科目平均分情况

4. **Assistant 提示词（Few-shot 示例）：**

```json
[
    {
        "title": "统计全校各科目平均分",
        "sql": "SELECT subject, ROUND(AVG(score), 2) AS avg_score FROM student_grades GROUP BY subject ORDER BY avg_score DESC;"
    },
    {
        "title": "统计各科目及格率",
        "sql": "SELECT subject, ROUND(COUNT(CASE WHEN score >= 60 THEN 1 END) * 100.0 / COUNT(*), 2) as pass_rate FROM student_grades GROUP BY subject ORDER BY pass_rate DESC;"
    },
    {
        "title": "统计各科目成绩分布",
        "sql": "SELECT subject, COUNT(CASE WHEN score >= 90 THEN 1 END) as excellent, COUNT(CASE WHEN score >= 75 AND score < 90 THEN 1 END) as good, COUNT(CASE WHEN score >= 60 AND score < 75 THEN 1 END) as pass, COUNT(CASE WHEN score < 60 THEN 1 END) as fail FROM student_grades GROUP BY subject;"
    }
]
```

### 3.3 直接回复：SQL 生成中

![SQL生成中提示](../../images/6.3/04.png)

**回复内容：**

```markdown
### SQL 正在生成中

```

> 这一步也可以省略，主要是为了提醒用户当前处理状态。

### 3.4 代码执行：格式转换

![格式转换节点](../../images/6.3/05.png)

**作用：** 从大模型输出的字符串中提取和解析 JSON 数据，返回字典形式

**输入变量：** `input_string: LLM/{x}text`

**代码：**

```python
import re
import json

def main(input_string: str) -> dict:
    pattern_match = re.search(r'```json\s*([\s\S]*?)\s*```', input_string)
    if not pattern_match:
        raise ValueError("输入字符串中未找到有效的 JSON 数据")
    json_content = pattern_match.group(1).strip()
    try:
        parsed_json = json.loads(json_content)
    except json.JSONDecodeError as err:
        raise ValueError(f"JSON 解析失败: {err}")
    return {"result": parsed_json}
```

**输出：** `result → Array[Object]`

### 3.5 直接回复：SQL 生成完毕

![SQL生成完毕提示](../../images/6.3/06.png)

**回复内容：**

```markdown
### SQL 生成完毕！

```

### 3.6 循环迭代

![循环迭代节点](../../images/6.3/07.png)

**作用：** 针对代码处理得到的字典结果中的每个元素（SQL 语句），循环执行后得到每个 SQL 的查询结果

| 配置项 | 值 |
|--------|-----|
| 输入 | `代码执行/{x}result Array[Object]` |
| 输出 | `SQL Execute/{x}jsonArray[Object]` |
| 错误处理 | 移除错误输出 |

### 3.7 循环体内部：代码执行（提取字段）

![循环体代码执行](../../images/6.3/08.png)

**作用：** 针对数组中的每个元素 dict，提取 title 和 sql 字段

**输入变量：** `args: 迭代/{x}item Object`

**代码：**

```python
def main(args: dict) -> dict:
    title = args.get("title", "")
    sql = args.get("sql", "")
    return {"title": title, "sql": sql}
```

### 3.8 循环体内部：SQL 执行

![循环体SQL执行](../../images/6.3/09.png)

**作用：** 执行 SQL 语句

**输入变量：** `循环体代码执行/{x}sql`

### 3.9 代码执行：结果格式转换

![结果格式转换](../../images/6.3/10.png)

**作用：** 对循环迭代的结果进行格式转换

**代码：**

```python
def main(args) -> dict:
    return {"result": "".join(str(item) for item in args)}
```

### 3.10 直接回复：结果汇总

![结果汇总提示](../../images/6.3/11.png)

**回复内容：**

```markdown
### SQL 计算完毕，模型正在汇总中...

```

### 3.11 大模型：回复结果

![大模型汇总节点](../../images/6.3/12.png)

**作用：** 对查询结果进行汇总分析，并把结果组装为 ECharts 图表需要的 JSON 格式数据

**配置：**

| 配置项 | 值 |
|--------|-----|
| 模型 | `qwen3-max` |
| 上下文 | `处理循环体结果/{x}result String` |

**系统 Prompt：**

```markdown
### 角色
你是一个数据分析师，需要基于前一个模型生成的SQL语句及其执行结果，优先针对用户问题进行回答，同时以JSON格式输出给用户。

### 图表使用场景
- 线性图：展示趋势变化数据（时间序列）
- 柱状图：比较不同类别间的数量或占比
- 饼状图：展示整体组成部分及比例

### 输出JSON格式
{
  "results": "用Markdown格式回复用户",
  "ECHarts": "1",
  "chartType": "线性图/柱状图/饼状图",
  "chartTitle": "图表标题",
  "chartData": "用;隔开的数据",
  "chartXAxis": "用;隔开的X轴"
}
```

### 3.12 代码执行：结果处理

![ECharts结果处理](../../images/6.3/13.png)

**作用：** 对大模型返回的结果进行解析，提取 ECharts 图表参数

**代码：**

```python
import re
import json

def main(args: str) -> dict:
    default_output = {
        "results": "", "ECHarts": "0",
        "chartType": "", "chartTitle": "",
        "chartData": "", "chartXAxis": ""
    }
    try:
        match = re.search(r'```json\s*([\s\S]*?)\s*```', args)
        if not match:
            raise ValueError("未找到有效JSON数据")
        results_dict = json.loads(match.group(1).strip())
    except:
        return default_output
    if results_dict.get("ECHarts") == "1":
        for f in ["chartType", "chartTitle", "chartData", "chartXAxis"]:
            results_dict.setdefault(f, "")
    return results_dict
```

### 3.13 直接回复

![结果文本](../../images/6.3/14.png)

**回复内容：** `代码执行生成ECHART/{x}results`

### 3.14 条件分支

![条件分支节点](../../images/6.3/15.png)

**作用：** 根据大模型返回的结果判断需要生成哪种图表（线性图/柱状图/饼图）

![条件分支配置](../../images/6.3/16.png)

### 3.15 ECharts 图表生成

![ECharts图表生成节点](../../images/6.3/17.png)

**输入参数（三种图表通用）：**

| 参数 | 来源 |
|------|------|
| 标题 | `代码执行生成ECHART/{x}chartTitle` |
| 数据 | `代码执行生成ECHART/{x}chartData` |
| X轴/分类 | `代码执行生成ECHART/{x}chartXAxis` |

![ECharts参数配置](../../images/6.3/18.png)

### 3.16 直接回复：结果生成

![结果生成](../../images/6.3/19.png)

### 3.17 结果展示

![结果展示1](../../images/6.3/20.png)
![结果展示2](../../images/6.3/21.png)
