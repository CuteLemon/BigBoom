## 原则

1. 可读性等于可维护性
2. 代码规范很重要
3. 会定期检查代码

## 规范

1. 所有关键字全部大写
2. 注释代码整体功能与关键点
3. 每行一个字段
4. 严禁嵌套子查询, 使用CTEs（Common Table Expressions）
5. 列名、表名、中间表名尽量有含义
6. 自定义函数 写明参数、测试用例

### 示例
```sql
/*
示例代码
	演示一个常规的查询任务
*/
WITH my_data AS (
 
   SELECT *  
   FROM analytics.my_data
   WHERE filter = 'my_filter'
 
), some_cte AS (
 
   SELECT DISTINCT
     id,
     other_field_1,
     other_field_2
   FROM analytics.my_other_data
 
)
 
SELECT 
	data_by_row['id']::bigint  AS id_field,
	field_1                    AS detailed_field_1,
	field_2                    AS detailed_field_2,
	detailed_field_3,
	CASE 
	 WHEN cancellation_date IS NULL AND expiration_date IS NOT NULL
	   THEN expiration_date
	 WHEN cancellation_date IS NULL
	   THEN start_date+7
	 ELSE cancellation_date
	END                        AS cancellation_date,
	SUM(field_4)               AS field_4_sum,
	MAX(field_5)               AS field_5_max
FROM my_data
LEFT JOIN some_cte ON my_data.id = some_cte.id 
WHERE 
	field_1 = 'abc'
	AND (field_2 = 'def' OR field_2 = 'ghi')
GROUP BY 
	id_field,
	detailed_field_1,
	detailed_field_2,
	detailed_field_3,
	cancellation_date
HAVING COUNT(*) > 1
ORDER BY 4 DESC
```

### 参考

[https://gist.github.com/fredbenenson/7bb92718e19138c20591](https://gist.github.com/fredbenenson/7bb92718e19138c20591)