import { model } from './model';
import { view } from './view';
import { PROJECT_CLASSES, TASK_CLASSES } from "./constants"

const controller = (function() {
    const init = function() {
        view.init();
        view.renderProjects();
    }
    const click = function(element) {
        switch (element.className) {
            case PROJECT_CLASSES.ADD:
                console.log("addButton was pressed");
                break;
            case PROJECT_CLASSES.TEXT:
                console.log("text was pressed");
                break;
            default:
                console.log("default");
        }
    }
    const prompt = function() {

    }
    return { init, click }
})();

export { controller };