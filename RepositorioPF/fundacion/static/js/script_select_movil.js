function showimage( fm ){
    if (!document.images) return
    ind = fm.ELEGIR.selectedIndex;
    sel = fm.ELEGIR.options[ind].value;
    document.images.GIF.src = "./COLORES/"+sel;
}