CREATE TABLE ads_categories (
	id BIGSERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	is_custom BOOLEAN NOT NULL,
	picture_url VARCHAR(200) NOT NULL
)