var Menu = new Class({
    Implements: [Options],
    options:{
        menu_li: '.menu_li',
        submenu_li: '.submenu_li',
        menu_ul: 'menu',
        submenu_ul: 'submenu'
    },
    initialize: function(element) {
        this.menus = $$(this.options.menu_li);

        this.menus.each(function(menu, index){
            menu.addEvents({
                mouseover: function(){
                    var sub = menu.getElement(this.options.submenu);
                    var tweenFx = new Fx.Tween('fxTarget', {
                        property: 'height',
                        duration: 500, 
                        transition: Fx.Transitions.Quart.easeInOut
                    });
                    tweenFx.start(0, 500);
                }.bind(this),
                mouseout: function(){
                    var sub = menu.getElement(this.options.submenu);
                    var tweenFx = new Fx.Tween('fxTarget', {
                        property: 'height',
                        duration: 500, 
                        transition: Fx.Transitions.Quart.easeInOut
                    });
                    tweenFx.start(500, 0);
                }.bind(this)
            })
        }.bind(this));
    }
});
window.addEvent('domready', function(){
    if ($$('.menus')) {
        var slide = new Menu($$('.menus')[0]);
    } 
});
