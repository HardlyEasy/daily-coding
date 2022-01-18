import { model } from './model';
import { view } from './view';

const controller = (function() {
    const init = function() {
        let defaultProject1 = model.createProject("DefaultProject1");
        model.addProject(defaultProject1);
        let defaultProject2 = model.createProject("DefaultProject2");
        model.addProject(defaultProject2);
        view.renderProjects();
    }
    const click = function(element){
        console.log("class: " + element.className)
    }
    return { init, click }
})();

export { controller };