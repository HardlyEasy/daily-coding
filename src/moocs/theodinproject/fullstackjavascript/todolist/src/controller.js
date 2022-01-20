import { model } from './model';
import { projectView, taskView } from './view';
import { PROJECT_CLASSES, TASK_CLASSES } from './constants'

const controller = (function() {
    const init = function() {
        projectView.init();
        taskView.init();
    }
    // Control based on clicked element class name
    const click = function(element) {
        switch (element.className) {
            case PROJECT_CLASSES.ADD: {
                let projectName = window.prompt('Enter project name: ');
                if (projectName === null || projectName === '')
                    break
                model.addProject(projectName);
                projectView.refresh();
            } break;
            case PROJECT_CLASSES.DELETE:
                model.removeProject(element.id.slice(1));
                projectView.refresh();
                break;
            case TASK_CLASSES.ADD: {
                let description = window.prompt('Enter task name: ');
                if (description === null || description === '')
                    break
                model.addTask(description, 'a', 'b');
                taskView.refresh();
            } break;
            case TASK_CLASSES.DELETE: {
                let modelListIndex = element.id.slice(1);
                model.removeTask(modelListIndex);
                taskView.refresh();
            } break;
            case PROJECT_CLASSES.TEXT: {
                let projectDiv = element.parentNode;
                let projectListIndex = projectDiv.id.slice(1);
                model.selectedProject = model.projectList[projectListIndex];
            } break;
            default:
                console.log('switch: default');
        }
        debugReport();
    }
    const debugReport = function() {
        console.log(model.getDebugReport());
    }
    return { init, click }
})();

export { controller };