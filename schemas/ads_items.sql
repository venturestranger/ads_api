CREATE TABLE ads_items (
	id BIGSERIAL PRIMARY KEY,
	id_author BIGINT NOT NULL,
	id_ads_category BIGINT NOT NULL,
	title VARCHAR(200) NOT NULL,
	picture_url VARCHAR(2000),
	content VARCHAR(5000) NOT NULL,
	date_publication TIMESTAMP NOT NULL,
	item_price FLOAT NOT NULL,
	location VARCHAR(150) NOT NULL,
	tel_id VARCHAR(60),
	inst_id VARCHAR(60),
	wa_id VARCHAR(50),
	phone VARCHAR(50) NOT NULL,
	CONSTRAINT fk_ads_categories_id
		FOREIGN KEY (id_ads_category)
		REFERENCES ads_categories (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);
