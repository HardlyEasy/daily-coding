import { currentUser } from './model'
import { controller } from './controller';
import { PROJECT_CLASSES, TASK_CLASSES } from './constants'

// Shared functions for taskView and projectView
const common = (function() {
    const createDiv = function(id, className, innerHTML) {
        let divElement = document.createElement('div');
        if (id !== '')
            divElement.id = id;
        if (className !== '')
            divElement.className = className;
        if (innerHTML !== '')
            divElement.innerHTML = innerHTML;
        return divElement;
    }
    const createImg = function(id, className, src) {
        let imgElement = document.createElement('img');
        if (id !== '')
            imgElement.id = id;
        if (className !== '')
            imgElement.className = className;
        if (src !== '')
            imgElement.src = src;
        imgElement.addEventListener('click', function() {
            controller.click(imgElement);
        });
        return imgElement;
    }
    // Remove all elements exact matching class
    const removeElements = function (removeClassName) {
        let element = document.getElementsByClassName(removeClassName);
        for (let i = element.length - 1; i >= 0; i--) {
            if (element[i].className === removeClassName)
                element[i].remove();
        }
    };
    return {
        createDiv, createImg,
        removeElements
    };
})();

const taskView = (function() {
    const rightDiv = document.getElementById('right-div');
    const init = function() {
        rightDiv.append(common.createDiv('', TASK_CLASSES.HEADER, 'Tasks'));
        rightDiv.append(
            common.createImg('', TASK_CLASSES.ADD, '../images/plus.svg'));
    }
    const refresh = function() {
        common.removeElements('task');
        render();
    };
    const render = function() {
        let taskList = currentUser.getTaskList();
        for (let i = 0; i < taskList.length; i++) {
            let task = taskList[i];
            let taskDiv = common.createDiv('t' + i, TASK_CLASSES.DIV, '')
            let textDiv = common.createDiv(
                '', TASK_CLASSES.TEXT, task.description);
            textDiv.addEventListener('click', function() {
                controller.click(textDiv);
            });
            let deleteImg = common.createImg(
                '', TASK_CLASSES.DELETE, '../images/delete.svg')
            taskDiv.append(textDiv, deleteImg);
            rightDiv.appendChild(taskDiv);
        }
    };
    return {
        init, refresh
    };
})();

const projectView = (function() {
    const leftDiv = document.getElementById('left-div');
    const init = function() {
        leftDiv.append(
            common.createDiv('', PROJECT_CLASSES.HEADER, 'Projects'));
        leftDiv.append(
            common.createImg('', PROJECT_CLASSES.ADD, '../images/plus.svg'));
    };
    const refresh = function() {
        common.removeElements('project');
        render();
    };
    const render = function() {
        for (let i = 0; i < currentUser.projectList.length; i++) {
            let project = currentUser.projectList[i];
            let projectDiv = common.createDiv('p' + i, PROJECT_CLASSES.DIV, '')
            let textDiv = common.createDiv(
                '', PROJECT_CLASSES.TEXT, project.name);
            textDiv.addEventListener('click', function() {
                controller.click(textDiv);
            });
            let deleteImg = common.createImg(
                '', PROJECT_CLASSES.DELETE, '../images/delete.svg')
            projectDiv.append(textDiv, deleteImg);
            leftDiv.appendChild(projectDiv);
        }
    };
    return {
        init, refresh
    };
})();

export {
    projectView, taskView
};