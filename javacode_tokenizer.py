import javalang
tree = javalang.parse.parse("package javalang.brewtab.com; class Test {}")
print tree
tokens = list(javalang.tokenizer.tokenize('System.out.println("Hello " + "world");'))
print tokens[6].value

path_test = "/if24/mr5ba/Masud/PythonProjects/dataset/autocode_data/test_data_code.txt"
java_code = open(path_test).read()
java_tokens = list(javalang.tokenizer.tokenize(java_code))

print java_tokens
text_file = open("java_tokens.txt", "w")
for i in range(0, len(java_tokens)):
    text_file.write(java_tokens[i])
text_file.close()