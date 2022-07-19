# 统一社会信用代码校验，生成；Social Unified Credit Code（SUCC）Generator, Validation

## 用法

### 名称

Social Unified Credit Code 简写 为 SUCC，

因此取名 succ_utils



### 安装 
```sh
pip install git+https://github.com/somenzz/social_unified_creditcode.git
```

### 使用
```python
# 随机一个统一社会信用代码
from succ_utils import CreditIdentifier

# 随机生成
ci = CreditIdentifier()
ret = ci.gen_random_credit_code()
print(ret)
#output {'address': '天津市天津市密云区', 'code': '92110118473154931H'} 
# 校验 
input_code = "914210031524040048"
print(ci.valid(input_code))
# False
```