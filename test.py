import random
import pymysql

def update_ballot(name):
  """随机增加票数。

  Args:
    name: 姓名。

  Returns:
    True 表示成功，False 表示失败。
  """
  # 连接数据库。
  conn = pymysql.connect(host="rm-hp30yyfd12f8023s8fo.mysql.huhehaote.rds.aliyuncs.com", port=3306, user="bpm_bridge", password="Fck53c0swla!$", database="qiaoliang")

  # 执行查询。
  cursor = conn.cursor()
  cursor.execute("update w_br_activity_cha set F_ballot = F_ballot + %s where F_name = %s", (random.randint(1, 12), name))

  # 提交事务。
  conn.commit()

  # 关闭连接。
  conn.close()

  return True


if __name__ == "__main__":
  # 姓名。
  name = "益阳青龙洲大桥"

  # 增加票数。
  success = update_ballot(name)

  if success:
    print(f"给 {name} 增加了 1 票。")
  else:
    print(f"给 {name} 增加票数失败。")