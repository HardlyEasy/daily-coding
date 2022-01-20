class Project {
    constructor (name) {
        this.name = name;
    }
}

class Task {
    constructor (description, dueDate, priority) {
        this.description = description;
        this.dueDate = dueDate;
        this.priority = priority;
    }
}

const model = (function() {
    let selectedProject;
    const projectList = [];
    const taskList = []
    const addProject = function(projectName) {
        projectList.push(new Project(projectName));
    }
    const addTask = function(description, dueDate, priority) {
        taskList.push(
            new Task(selectedProject, description, dueDate, priority));
    }
    const removeProject = function (i) {
        projectList.splice(i, 1);
    }
    const removeTask = function (i) {
        taskList.splice(i, 1);
    }
    const getDebugReport = function() {
        return {
            selectedProject, projectList, taskList
        }
    }
    return {
        projectList, taskList,
        addProject, removeProject,
        addTask, removeTask,
        getDebugReport
    }
})();

export { model }