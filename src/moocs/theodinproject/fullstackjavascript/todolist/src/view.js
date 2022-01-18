import { model } from "./model"
import { controller } from "./controller";

const CLASS_PROJECT = "project";
const CLASS_PROJECT_BUTTON = CLASS_PROJECT + " button";
const CLASS_PROJECT_TEXT = CLASS_PROJECT + " text"

const CLASS_TASK = "task";
const CLASS_TASK_BUTTON = CLASS_TASK + " button";
const CLASS_TASK_TEXT = CLASS_TASK + " text"

const view = (function() {
    const leftDiv = document.getElementById("left-div");
    const makeElement = function(elementName, className, textStr) {
        let element = document.createElement(elementName);
        if (className !== "")
            element.className = className;
        if (textStr !== "") {
            let textNode = document.createTextNode(textStr);
            element.appendChild(textNode);
        }
        return element
    }
    const addProject = function(elementName, className, project) {
        let projectDiv = makeElement("div", CLASS_PROJECT, "");
        let textDiv = makeElement("div", CLASS_PROJECT_TEXT, project.name);
        textDiv.addEventListener("click", function() {
           controller.click(textDiv);
        });
        projectDiv.appendChild(textDiv);
        leftDiv.appendChild(projectDiv);
    }
    const renderProjects = function() {
        for (let i = 0; i < model.projectList.length; i++) {
            let project = model.projectList[i];
            addProject("div", CLASS_PROJECT, project);
        }
    }
    return { addProject, renderProjects };
})();

export { view };