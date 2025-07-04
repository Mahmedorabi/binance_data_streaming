CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS ohlcv (
    id         UUID PRIMARY KEY,
    timestamp  BIGINT NOT NULL,
    open       NUMERIC NOT NULL,
    high       NUMERIC NOT NULL,
    low        NUMERIC NOT NULL,
    close      NUMERIC NOT NULL,
    volume     NUMERIC NOT NULL
);
