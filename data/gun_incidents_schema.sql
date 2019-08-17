-- postgres schema used to create gun incidents table within gun_violence database

create table gun_incidents (
	incident_id SERIAL,
	incident_date DATE NOT NULL,
	state varchar(30),
	city_or_county varchar(50),
	address varchar(60),
	number_killed integer,
	number_injured integer,
	CONSTRAINT pk_gun_incidents PRIMARY KEY (
		incident_id
	)
);