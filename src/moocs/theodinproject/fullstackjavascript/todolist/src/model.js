class Project {
    constructor (name) {
        this.name = name;
        this.taskList = []
    }
    addTask(task) {
        try {
            if (!(task instanceof Task))
                throw 'addTask: Expected task object type'
            this.taskList.push(task);
        } catch(e) {
            console.log(e);
        }
    }
    removeTask(index) {
        this.taskList.splice(index, 1);
    }
}

class Task {
    constructor (description, priority) {
        this.description = description;
        this.priority = priority;
    }
}

class User {
    constructor () {
        this.projectList = []
        this.projectIndex = null; // selected or active project
    }
    getProject() {
        return this.projectList[this.projectIndex];
    }
    setProjectIndex(projectIndex) {
        this.projectIndex = projectIndex;
    }
    addProject(project) {
        try {
            if (!(project instanceof Project))
                throw 'addProject: Expected project object type'
            this.projectList.push(project);
        } catch(e) {
            console.log(e);
        }
    }
    removeProject(index) {
        this.projectList.splice(index, 1);
    }
}

// TODO: I may add multiple user profile feature later
const currentUser = new User();
const defaultProject = new Project("DefaultProject");
defaultProject.addTask(new Task("DefaultTask0", 0));
defaultProject.addTask(new Task("DefaultTask1", 1));
currentUser.setProjectIndex(0);
currentUser.addProject(defaultProject);
currentUser.project = defaultProject;

export {
    Project, Task, currentUser
};