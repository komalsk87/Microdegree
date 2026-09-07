from sklearn.preprocessing import LabelEncoder

catagory = ['cat', 'dog', 'cat', 'fish', 'dog','bird']

encode = LabelEncoder()

encoder_feature = encode.fit_transform(catagory)

print(encoder_feature)