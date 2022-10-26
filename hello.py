print("Hello World")
def labels = jenkins.getLabels()
labels.each {
   println "${it.displayName}"
}
