class Project {
    constructor (name) {
        this.name = name;
    }
}

class Task extends Project {
    // Takes project object
    constructor(project, description, dueDate, priority) {
        super(project.name);
        this.description = description;
        this.dueDate = dueDate;
        this.priority = priority;
    }
}

const model = (function() {
    const projectList = [];
    const taskList = []
    // TODO: Limit character length allowed
    const createProject = function(projectName) {
        return new Project(projectName);
    }
    // TODO: Guard against invalid dates, limit length?
    const createTask = function(project, description, dueDate, priority) {
        return new Task(project, description, dueDate, priority);
    }
    const addProject = function(project) {
        projectList.push(project);
    };
    const addTask = function(task) {
        taskList.push(task);
    }
    return {
        projectList, taskList,
        createProject, createTask,
        addProject, addTask
    }
})();

export { model }