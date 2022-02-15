def create_classes(db, wineModel):
    if wineModel == 1:
        class WineQualityRed(db.Model):
            __tablename__ = 'winequalityRed'       

            fixed_acidity = db.Column('fixed acidity', db.Float)
            volatile_acidity = db.Column('volatile acidity', db.Float)	
            citric_acid = db.Column('citric acid', db.Float)	
            residual_sugar = db.Column('residual sugar', db.Float)	
            chlorides = db.Column(db.Float)	
            free_sulfur_dioxide = db.Column('free sulfur dioxide', db.Float)	
            total_sulfur_dioxide = db.Column('total sulfur dioxide', db.Float)	
            density = db.Column(db.Float)	
            pH = db.Column(db.Float)	
            sulphates = db.Column(db.Float)	
            alcohol = db.Column(db.Float)	
            quality = db.Column(db.Float)

            def __repr__(self):
                return '<Red Quality Score %r>' % (self.quality)
        return WineQualityRed
        
    elif wineModel == 2:

        class WineQualityWhite(db.Model):
            __tablename__ = 'winequalityWhite'       

            fixed_acidity = db.Column('fixed acidity', db.Float)
            volatile_acidity = db.Column('volatile acidity', db.Float)	
            citric_acid = db.Column('citric acid', db.Float)	
            residual_sugar = db.Column('residual sugar', db.Float)	
            chlorides = db.Column(db.Float)	
            free_sulfur_dioxide = db.Column('free sulfur dioxide', db.Float)	
            total_sulfur_dioxide = db.Column('total sulfur dioxide', db.Float)	
            density = db.Column(db.Float)	
            pH = db.Column(db.Float)	
            sulphates = db.Column(db.Float)	
            alcohol = db.Column(db.Float)	
            quality = db.Column(db.Float)

            def __repr__(self):
                return '<White Quality Score %r>' % (self.quality)
        return WineQualityWhite