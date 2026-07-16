# MySQL 数据库操作教程

本教程指导如何在 MySQL 数据库中创建学生成绩表（`student_grades`）并插入测试数据，为 NLP2SQL 数据库查询工作流准备数据源。

## 步骤 1：安装与准备 MySQL

- **下载安装：** 从 [MySQL 官网](https://dev.mysql.com/downloads/) 下载 Community Server
- **验证安装：** 终端输入 `mysql --version` 检查
- **启动服务：** Linux/Mac 运行 `sudo service mysql start`，Windows 通过服务管理器启动

## 步骤 2：登录 MySQL

```bash
# 本地登录
mysql -u root -p

# 远程服务器
mysql -u root -h 192.168.1.100 -p
```

- `-u root`：指定用户名
- `-p`：提示输入密码
- `-h`：远程服务器 IP 地址

**常见错误：**

| 错误信息 | 原因 | 解决方案 |
|---------|------|---------|
| Access denied | 密码错误 | 重置密码 |
| Command not found | MySQL 未加入 PATH | 配置环境变量 |

## 步骤 3：创建数据库

```sql
CREATE DATABASE dify_test;
USE dify_test;

-- 验证
SHOW DATABASES;
```

## 步骤 4：创建表

```sql
CREATE TABLE student_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    class_name VARCHAR(50) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    exam_date DATE NOT NULL,
    semester VARCHAR(50) NOT NULL,
    grade VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

**字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INT (自增) | 主键 |
| student_id | VARCHAR(20) | 学号 |
| student_name | VARCHAR(50) | 学生姓名 |
| class_name | VARCHAR(50) | 班级 |
| subject | VARCHAR(50) | 科目 |
| score | DECIMAL(5,2) | 分数（总长5位，小数2位） |
| exam_date | DATE | 考试日期 |
| semester | VARCHAR(50) | 学期 |
| grade | VARCHAR(50) | 年级 |
| created_at | DATETIME | 记录创建时间 |
| updated_at | DATETIME | 记录更新时间 |

## 步骤 5：插入数据

插入 100 条测试数据，涵盖高一至高三多个班级的各类科目成绩：

```sql
INSERT INTO student_grades (student_id, student_name, class_name, subject, score, exam_date, semester, grade, created_at, updated_at) VALUES 
('2023001', '李一', '高一(1)班', '数学', 85.00, '2023-09-15', '2023-2024学年第一学期', '高一', NOW(), NOW()),
('2023002', '王二', '高一(1)班', '英语', 92.50, '2023-09-20', '2023-2024学年第一学期', '高一', NOW(), NOW()),
('2023003', '张三', '高一(2)班', '物理', 78.00, '2023-10-05', '2023-2024学年第一学期', '高一', NOW(), NOW()),
-- ... 更多数据
('2023110', '陈十', '高二(1)班', '英语', 75.00, '2024-07-15', '2024-2025学年第一学期', '高二', NOW(), NOW());
```

> 完整 100 条 INSERT 语句见课程配套资源。

## 步骤 6：验证数据

```sql
-- 查看总记录数（应返回 100）
SELECT COUNT(*) FROM student_grades;

-- 查看前 10 条
SELECT * FROM student_grades LIMIT 10;

-- 描述表结构
DESCRIBE student_grades;
```

## 步骤 7：退出 MySQL

```sql
EXIT;
-- 或
QUIT;
```
