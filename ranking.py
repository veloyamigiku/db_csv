from datetime import datetime
import os
import pandas as pd

from input.ranking_data import ranking_data

output_dir = "output"

if not os.path.isdir(output_dir):
  os.makedirs(output_dir)

ranking_list = []
id = 0
now = datetime.now()
for ranking in ranking_data:
  title = ranking["title"]
  url = ranking["url"]
  img_url = ranking["imgUrl"]
  dt = now.strftime('%Y/%m/%d %H:%M:%S')
  ranking_list.append([
    id,
    title,
    url,
    img_url,
    dt,
    dt])
  id += 1

ranking_df = pd.DataFrame(
  ranking_list,
  columns=[
    "id",
    "title",
    "url",
    "img_url",
    "created_at",
    "updated_at"])
print("ranking_df:\n", ranking_df)
ranking_df.to_csv(
  output_dir + os.sep + "ranking.csv",
  encoding="SHIFT_JIS",
  index=False)
