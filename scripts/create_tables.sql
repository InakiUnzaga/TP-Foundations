CREATE TABLE goalscorers (
	id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	home_team VARCHAR(100) NOT NULL,
	away_team VARCHAR(100) NOT NULL,
	team VARCHAR(100) NOT NULL,
	scorer VARCHAR(100) NOT NULL,
	minute INTEGER,
	own_goal BOOLEAN,
	penalty BOOLEAN
);
