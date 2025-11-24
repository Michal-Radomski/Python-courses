from imageai.Classification import ImageClassification  # type: ignore
import os

exec_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()

predctions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, "godzilla.jpg"), result_count=5
)
for eachPred, eachProb in zip(predctions, probabilities):
    print(f"{eachPred} : {eachProb}")

# boathouse : 97.1359
# mobile home : 0.6925
# lakeside : 0.5863
# beacon : 0.431
# dam : 0.1176

# impala : 29.0923
# German short-haired pointer : 17.2527
# zebra : 13.7695
# gazelle : 11.4433
# llama : 6.3483

# common iguana : 47.002
# American alligator : 32.1232
# triceratops : 9.9207
# frilled lizard : 6.3106
# African crocodile : 0.3448
