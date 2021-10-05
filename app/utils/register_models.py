def register_models(namespace, model_dict_arr):
    for model_dict in model_dict_arr:
        print(model_dict)
        for key in model_dict.keys():
            print(key)
            namespace.models[key] = model_dict[key]