print("Hello World")
def jenkins = Jenkins.instance
def computers = jenkins.computers
computers.each {
   println "${it.displayName} ${it.hostName}"
}
