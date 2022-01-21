import { Project, Task, currentUser } from './model';
import { projectView, taskView } from './view';
import { PROJECT_CLASSES, TASK_CLASSES } from './constants'

const controller = (function() {
    const init = function() {
        projectView.init();
        projectView.refresh();
        taskView.init();
        taskView.refresh();
        console.log(currentUser);
    }
    const click = function(element) {
        switch (element.className) {
            case PROJECT_CLASSES.ADD: {
                let projectName = window.prompt('Enter project name: ');
                if (projectName === null || projectName === '')
                    break
                currentUser.addProject(new Project(projectName));
            } break;
            case PROJECT_CLASSES.DELETE: {
                let projectListIndex = parseInt(
                    element.parentElement.id.slice(1));
                currentUser.removeProject(projectListIndex);
            } break;
            case PROJECT_CLASSES.TEXT: {
                let projectIndex = parseInt(
                    element.parentElement.id.slice(1));
                currentUser.setProjectIndex(projectIndex);
            } break;
            case TASK_CLASSES.ADD: {
                let description = window.prompt('Enter task name: ');
                if (description === null || description === '')
                    break
                currentUser.getProject().addTask(new Task(description, 0))
            } break;
            case TASK_CLASSES.DELETE: {
                let taskListIndex = parseInt(
                    element.parentElement.id.slice(1));
                currentUser.getProject().removeTask(taskListIndex);
            } break;
            default:
                console.log('switch: default');
        }
        projectView.refresh();
        taskView.refresh();
        console.log(currentUser);
    }
    return {
        init, click
    };
})();

export { controller };