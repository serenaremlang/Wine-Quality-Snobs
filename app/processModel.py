import numpy as np
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

    score = []
    score.append(3) # 3 means we got nothing good going on

    input = np.array([fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol])
    f_input = input.astype(np.float)
    print(f_input)
    # print(f'input:{float(input)}')
    if model_type == '1': # if red...
        from red_model import red_model
        score = red_model(f_input)
        print(f'red:{score[0]}')

    elif model_type == '2': # if white...
        # use the vars passed in above and render the white predicition score
        from white_model import white_model
        score = white_model(f_input)
        print(f'white:{score[0]}')

    print(f'returning: {score[0]}')
    print(f'type: {type(score)}')
    return score[0].astype(str)