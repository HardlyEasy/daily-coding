import { Project } from './project'

class Task extends Project {
    constructor(projectName, description, dueDate, priority) {
        super(projectName);
        this.description = description;
        this.dueDate = dueDate;
        this.priority = priority;
    }
}

const taskView = (function() {
    const rightDiv = document.getElementById("right-div");
    const init = function () {

    };
    return { init }
})();

export { taskView }