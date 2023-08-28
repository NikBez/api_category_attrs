def get_product_analitic_query(category_id: str, product_id: str):
    return f'''
   WITH empty_values AS (
	SELECT 
		c.category_id id,
		count() empty_value
	FROM 
		categories c 
	JOIN category_attrs ca ON c.category_id = ca.category_id
	LEFT JOIN product_attr pa ON ca.attribute_id = pa.attribute_id 
	WHERE 
		c.category_id = '{category_id}' AND pa.product_id = '{product_id}' AND (isNull(pa.value) OR pa.value='')
	GROUP BY id
),
annotation_length AS (
	SELECT 
		c.category_id id,
		pa.value annotation,
		lengthUTF8(pa.value) annotation_length
	FROM 
		categories c 
	JOIN category_attrs ca ON c.category_id = ca.category_id
	LEFT JOIN product_attr pa ON ca.attribute_id = pa.attribute_id 
	WHERE 
		c.category_id = '{category_id}' AND pa.product_id = '{product_id}' AND ca.attribute_name = 'Аннотация'
	GROUP BY 
		id, pa.value
),
images_count AS (
	SELECT 
		c.category_id id,
		pa.value images,
		LENGTH(splitByChar(';', pa.value)) images_count
	FROM 
		categories c 
	JOIN category_attrs ca ON c.category_id = ca.category_id
	LEFT JOIN product_attr pa ON ca.attribute_id = pa.attribute_id 
	WHERE 
		c.category_id = '{category_id}' AND pa.product_id = '{product_id}' AND ca.attribute_name = 'images'
	GROUP BY 
		id, pa.value
),
required_values AS (
	SELECT 
	c.category_id id,
    groupArray(pa.value) required_values
	FROM 
	    categories c 
	JOIN category_attrs ca ON c.category_id = ca.category_id
	LEFT JOIN product_attr pa ON ca.attribute_id = pa.attribute_id 
	WHERE 
	    c.category_id = '{category_id}' AND pa.product_id = '{product_id}' AND ca.required=True
	GROUP BY 
		id
)
select distinct
	count(pa.value) OVER() total_count,
	FLOOR(ev.empty_value / (total_count / 100)) blank_percentage,
	al.annotation_length annotation_length,
	ic.images_count images_count,
	al.annotation annotation,
	ic.images images,
	rv.required_values required_values	
from categories c
	join category_attrs ca on c.category_id = ca.category_id 
	left join product_attr pa on ca.attribute_id = pa.attribute_id
	left join empty_values ev on c.category_id = ev.id
	left join annotation_length al on c.category_id = al.id
	left join images_count ic on c.category_id = ic.id
	left join required_values rv on c.category_id = rv.id
where
	c.category_id = '{category_id}'
	and pa.product_id = '{product_id}'
'''
