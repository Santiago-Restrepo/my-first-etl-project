CREATE TABLE "location" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "author" (
  "id" varchar PRIMARY KEY,
  "num_reviews" integer,
  "username" varchar,
  "location_id" integer
);

CREATE TABLE "review" (
  "id" integer PRIMARY KEY,
  "rating_id" integer,
  "author_id" varchar,
  "text" text,
  "date" date,
  "hotel_id" integer
);

CREATE TABLE "ratings" (
  "id" integer PRIMARY KEY,
  "service" float,
  "cleanliness" float,
  "overall" float,
  "value" float,
  "location" float,
  "sleep_quality" float,
  "rooms" float
);

CREATE TABLE "hotel" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "stars" float,
  "address_id" integer,
  "url" text
);

CREATE TABLE "address" (
  "id" integer PRIMARY KEY,
  "region" varchar,
  "street_address" varchar,
  "postal_code" varchar,
  "locality" varchar
);

ALTER TABLE "author" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id");

ALTER TABLE "ratings" ADD FOREIGN KEY ("id") REFERENCES "review" ("rating_id");

ALTER TABLE "author" ADD FOREIGN KEY ("id") REFERENCES "review" ("author_id");

ALTER TABLE "address" ADD FOREIGN KEY ("id") REFERENCES "hotel" ("address_id");

ALTER TABLE "hotel" ADD FOREIGN KEY ("id") REFERENCES "review" ("hotel_id");
