import sys
import data
import models
import matplotlib.pyplot as plt

training_set, testing_set = data.readFile(sys.argv[1])
training_X, training_Y = models.features_labels(training_set)
testing_X, testing_Y = models.features_labels(testing_set)
model, err = models.gbr(training_X, training_Y, testing_X, testing_Y)
prediction = model.predict(testing_X)
diff = [ testing_Y[i] - prediction[i] for i in range(len(testing_Y))]
plt.plot(testing_Y, diff, 'bo')
plt.axhline(0, color='red')
plt.savefig(r"figure_1.png")
