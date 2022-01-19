import { model } from "./model"
import { controller } from "./controller";
import { PROJECT_CLASSES, TASK_CLASSES } from "./constants"

// TODO: maybe a better way of doing constants here


const view = (function() {
    const leftDiv = document.getElementById("left-div");
    const init = function() {
        let projectTitle = document.createElement("div");
        projectTitle.className = PROJECT_CLASSES.HEADER;
        projectTitle.innerHTML = "Projects";
        leftDiv.appendChild(projectTitle);
        let imgElement = document.createElement("img");
        imgElement.src = "../images/plus.png";
        imgElement.className = PROJECT_CLASSES.ADD;
        imgElement.addEventListener("click", function() {
            controller.click(imgElement);
        });
        leftDiv.append(projectTitle, imgElement);
    }
    const addProject = function(elementName, className, project) {
        // project div has children of textDiv and imageDiv
        let projectDiv = document.createElement("div");
        projectDiv.className = PROJECT_CLASSES.DIV;
        let textDiv = document.createElement("div");
        textDiv.className = PROJECT_CLASSES.TEXT;
        textDiv.innerHTML = project.name;
        textDiv.addEventListener("click", function() {
            controller.click(textDiv);
        });
        projectDiv.appendChild(textDiv);
        leftDiv.appendChild(projectDiv);
    };
    const renderProjects = function() {
        for (let i = 0; i < model.projectList.length; i++) {
            let project = model.projectList[i];
            addProject("div", PROJECT_CLASSES.DIV, project);
        }
    };
    return { init, addProject, renderProjects };
})();

export { view };