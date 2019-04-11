# Flask 项目模板接口文档

版本：v0.0.1

## 获取作者信息

功能说明：根据数据库连接信息获取数据库信息

`GET`：`/api/v3/template/info`


#### 返回示例

状态码：200

```json
{
    "name": "Shi Tao",
    "area": "Shanghai",
    "age": 22
}
```

|参数名称| 描述 |
|:---:|:---:|
|name|作者|
|area|地区|
|age|年龄|

### 错误列表

|状态码|内容|描述|
|:--:|:---:|:---:|
|500|{"message":"no such server"}|服务器不存在|