import pandas as pd
import numpy as np
# 샘플 데이터 생성
np.random.seed(42)
data = {
 "employee_id": range(1, 51),
 "age": np.random.randint(23, 60, 50),
 "experience_years": np.random.randint(1, 30, 50),
 "monthly_salary": np.random.randint(300, 900, 50),
 "performance_score": np.random.randint(1, 100, 50)
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
print("sample_data.csv 생성 완료!")