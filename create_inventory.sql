CREATE TABLE IF NOT EXISTS inventory
(
    item_no integer NOT NULL,
    item_name text NOT NULL,
    category text  NOT NULL,
    stock_qty integer NOT NULL,
    CONSTRAINT inventory_pkey PRIMARY KEY (item_no)
);