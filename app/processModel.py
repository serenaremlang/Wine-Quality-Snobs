def getWineScore(
    fixed_acidity,
    volatile_acidity,	
    citric_acid,
    residual_sugar,	
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    pH,
    sulphates,
    alcohol,
    model_type
):
    print(f'model: {model_type}')
    print(f'model: {type(model_type)}')

    score = 3 # 3 means we got nothing good going on

    input = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]

    if model_type == '1': # if red...
        # use the vars passed in above and render the red predicition score
        score = 2
        print(f'red:{score}')

    elif model_type == '2': # if white...
        # use the vars passed in above and render the white predicition score
        from white_model import white_model
        score = white_model(input)
        print(f'white:{score}')

    print(f'returning: {score}')
    return score