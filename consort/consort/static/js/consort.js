onclick = (event) => {
    const collapseElementList = [].slice.call(document.querySelectorAll('[data-te-collapse-item]'))
    const collapseList = collapseElementList.forEach((collapseEl) => {
        if (collapseEl.contains(event.target)) {
            return;
        }
        const myCollapse = new te.Collapse(collapseEl, {toggle: false});
        myCollapse.hide();
    });
}
