class Project {
    constructor (projectName, taskList) {
        this.projectName = projectName;
    }
}

const projectModel = (function() {
    const projects = [new Project("DefaultProject")];
    const add = function(projectName) {
        projects.push(new Project(projectName));
    };
    return { projects, add }
})();

const projectView = (function() {
    const leftDiv = document.getElementById("left-div");
    /* Convenience function */
    const addElement = function(elementName, className, text) {
        let element = document.createElement(elementName);
        if (className !== "")
            element.className = className;
        let textNode = document.createTextNode(text);
        element.appendChild(textNode);
        leftDiv.appendChild(element);
    }
    const init = function () {
        render();
    }
    const render = function() {
        for (let i = 0; i < projectModel.projects.length; i++) {
            let p = projectModel.projects[i];
            addElement("div", "project-text", p.projectName);
        }
    }
    const clear = function() {

    }
    return { init, render };
})();

export { Project, projectView }