-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	username varchar NULL,
	"password" varchar NULL,
	id serial4 NOT NULL,
	"name" varchar NULL,
	familyname varchar NULL,
	address varchar NULL,
	phonenumber varchar NULL,
	email varchar NULL,
	creationdate timestamp NULL,
	state bool NULL,
	CONSTRAINT user_pk PRIMARY KEY (id),
	CONSTRAINT user_un UNIQUE (username, email, id)
);

-- public.sale definition

-- Drop table

-- DROP TABLE public.sale;

CREATE TABLE public.sale (
	id serial4 NOT NULL,
	user_id serial4 NOT NULL,
	worth int4 NOT NULL,
	quantity int4 NULL,
	CONSTRAINT sale_pk PRIMARY KEY (id)
);


-- public.sale foreign keys

ALTER TABLE public.sale ADD CONSTRAINT sale_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;