from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# 认证令牌，Dify配置必须和这里一致
VALID_TOKEN = "itcast"

# 国内城市编码，可自行扩充
CITY_CODES = {
    "北京": "101010100",
    "上海": "101020100",
    "广州": "101280101",
    "深圳": "101280601",
    "杭州": "101210101",
    "成都": "101270101",
    "武汉": "101200101",
    "西安": "101110101",
    "南京": "101190101",
    "重庆": "101040100",
    "郑州": "101180101"
}

# 请求参数模型
class WeatherRequest(BaseModel):
    location: str

# 天气查询POST接口
@app.post("/weather")
def get_current_weather(request: Request, body: WeatherRequest):
    # 校验Bearer Token
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {VALID_TOKEN}":
        raise HTTPException(status_code=403, detail="令牌错误，访问被拒绝")
    
    location = body.location
    city_code = CITY_CODES.get(location)
    if not city_code:
        return {
            "status": "error",
            "message": f"暂不支持{location}，可查询城市：{','.join(CITY_CODES.keys())}"
        }
    
    # 请求公共天气API
    try:
        res = requests.get(f"http://t.weather.itboy.net/api/weather/city/{city_code}", timeout=10)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        return {"status": "error", "message": f"天气接口请求失败：{str(e)}"}
    
    # 解析当日天气
    try:
        forecast = data["data"]["forecast"][0]
        weather_type = forecast["type"]
        high = forecast["high"].replace("高温 ", "")
        low = forecast["low"].replace("低温 ", "")
        return f"{location}今日天气：{weather_type}，气温{low}-{high}"
    except Exception as e:
        return {"status": "error", "message": f"数据解析失败：{str(e)}"}

# 启动服务入口
if __name__ == "__main__":
    import uvicorn
    # 监听0.0.0.0，端口8081
    uvicorn.run(app, host="0.0.0.0", port=8081)