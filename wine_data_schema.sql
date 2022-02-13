CREATE TABLE "winequalityRed" (
	"wine_id"	INTEGER NOT NULL UNIQUE,
	"fixed acidity"	INTEGER NOT NULL,
	"volatile acidity"	INTEGER NOT NULL,
	"citric acid"	INTEGER NOT NULL,
	"residual sugar"	INTEGER NOT NULL,
	"chlorides"	INTEGER NOT NULL,
	"free sulfur dioxide"	INTEGER NOT NULL,
	"total sulfur dioxide"	INTEGER NOT NULL,
	"density"	INTEGER NOT NULL,
	"pH"	INTEGER NOT NULL,
	"sulphates"	INTEGER NOT NULL,
	"alcohol"	INTEGER NOT NULL,
	"quality"	INTEGER NOT NULL,
	PRIMARY KEY("wine_id")
)

CREATE TABLE "winequalityWhite" (
	"wine_id"	INTEGER NOT NULL UNIQUE,
	"fixed acidity"	INTEGER NOT NULL,
	"volatile acidity"	INTEGER NOT NULL,
	"citric acid"	INTEGER NOT NULL,
	"residual sugar"	INTEGER NOT NULL,
	"chlorides"	INTEGER NOT NULL,
	"free sulfur dioxide"	INTEGER NOT NULL,
	"total sulfur dioxide"	INTEGER NOT NULL,
	"pH"	INTEGER NOT NULL,
	"sulphates"	INTEGER NOT NULL,
	"alcohol"	INTEGER NOT NULL,
	"quality"	INTEGER NOT NULL,
	"density"	INTEGER NOT NULL,
	PRIMARY KEY("wine_id")
)