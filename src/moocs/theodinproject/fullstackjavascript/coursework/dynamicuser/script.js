window.onclick = function(event) {
    // if click anywhere besides button, remove invisible class from items
    if (!event.target.matches('.dropdown-button')) {
        let itemsDiv = document.getElementsByClassName("dropdown-items");
        for (let i = 0; i < itemsDiv.length; i++) {
            let item = itemsDiv[i];
            if (item.classList.contains('visible')) {
                item.classList.remove('visible');
            }
        }
    }
};

const view = (function() {
    const header = document.getElementById("header");
    // Create .dropdown div element
    const createDropdown = function(linkHrefList, linkTextList) {
        let dropdownDiv = document.createElement("div");
        dropdownDiv.className = 'dropdown';
        let button = document.createElement("button");
        button.className = 'dropdown-button';
        button.textContent = 'Links';
        let itemsDiv = createItems(linkHrefList, linkTextList);
        button.onclick = function() {
            console.log('Toggling dropdown...');
            itemsDiv.classList.toggle("visible");
        };
        dropdownDiv.append(button, itemsDiv);
        return dropdownDiv;
    }
    // Create .dropdown-items div element
    const createItems = function(linkHrefList, linkTextList) {
        let itemsDiv = document.createElement("div");
        itemsDiv.className = 'dropdown-items';
        for (let i = 0; i < linkTextList.length; i++) {
            let item = document.createElement("a");
            item.href = linkHrefList[i];
            item.innerText = linkTextList[i];
            itemsDiv.append(item);
        }
        return itemsDiv
    }
    return {
        header,
        createDropdown
    }
})();

view.header.append(view.createDropdown(['#','#'], ['Link1', 'Link2']));
view.header.append(view.createDropdown(['#','#'], ['Link3', 'Link4']));