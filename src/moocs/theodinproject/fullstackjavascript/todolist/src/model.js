class Project {
    constructor (name) {
        this.name = name;
        let defaultTask = new Task("defaultDescription", "01-01-2022", "High");
        this.taskList = [defaultTask]
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
        let defaultProject = new Project("DefaultProject")
        this.projectList = new Array(defaultProject);
        this.project = defaultProject; // selected or active project
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
    addTask(task) {
        try {
            if (!(task instanceof Task))
                throw 'addTask: Expected task object type'
            this.project.taskList.push(task);
        } catch(e) {
            console.log(e);
        }
    }
    getTaskList() {
        return this.project.taskList;
    }
}

// TODO: I may add multiple user profile feature later
const currentUser = new User();

export {
    Project, Task, currentUser
};