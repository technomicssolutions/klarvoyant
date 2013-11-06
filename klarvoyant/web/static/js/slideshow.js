var ImageSlider = new Class({
    Implements: [Options],
    options:{
        imageSliderDiv: '.slideshow',
        slideshowContainer: '.banner',
        controlDiv: 'controls',
        delay: 5000,
        effectDuration: 500,
        startMargin: 0,
        minMargin: -1550,
        maxMargin: 1550,
        activeOptions : {
            'transition' : 'elastic:out',
            'duration' : 1500
        },
        slideOptions: {   
            'transition' : 'back:in:out', 
            'duration' : 1000,
            'link': 'cancel'
        }
    },
    initialize: function(element) {
        this.element = $(element);
        this.imgs = this.element.getElements('img');
        this.setImgMargin();
        this.controldiv = $(this.options.controlDiv);
        this.controls = this.controldiv.getElements('a');
        this.hidden_controls = this.controldiv.getElements('.hidden');
        
        this.activeSlide = $$('.slide_active').set('tween', this.options.activeOptions);
        this.initialLeft = parseInt(this.activeSlide.getStyle('left'));
        this.activeLeft = 35;
        this.changeLeft = 0;
        this.currentIndex = 0;
        this.nextIndex = 1;
        this.timer = null;
        this.clicked = false;
        this.currentImage = this.imgs[this.currentIndex];
        this.currentImage.setStyle('margin-left', this.options.startMargin);
        if (this.imgs.length == 2)
            this.controls[2].setStyle('display','none');
        if (this.imgs.length > 1) {
            this.nextImage = this.imgs[this.nextIndex];
            this.effects = new Fx.Elements(this.imgs, this.options.slideOptions);
            this.effects.addEvent('complete', function() {
                if (!this.clicked) {
                    this.timer = this.autoSlide.delay(this.options.delay, this);
            
                }
            }.bind(this));

            this.controls.each(function(control, index) {
                control.addEvent('click', function(ev) {
                    ev.stop();
                    if(index!=this.currentIndex) {
                        this.clicked = true;
                        this.slideOnClick(index);
                    }
                }.bind(this));  
            }.bind(this));
            this.timer = this.autoSlide.delay(this.options.delay, this);
        }
        else 
            this.controldiv.setStyle('display','none');
    },
    transition: function(currentImage, nextImage, clicked) {
        this.controls[this.currentIndex].removeClass('active').addClass('inactive');
        var effect = {};
        flag = 0
        if(clicked) {
            flag = (this.currentIndex > this.nextIndex) ? 1 : 0;
            // this.effects.cancel();
        } 
        if (flag==0){
            effect[this.currentIndex] = {'margin-left': [this.options.startMargin, this.options.minMargin]};
            effect[this.nextIndex] = { 'margin-left': [this.options.maxMargin, this.options.startMargin]};
        } else {
            effect[this.currentIndex] = {'margin-left': [this.options.startMargin, this.options.maxMargin]};
            effect[this.nextIndex] = { 'margin-left': [this.options.minMargin, this.options.startMargin]};    
        }

        this.changeLeft = this.initialLeft + (this.activeLeft*this.nextIndex); 
        this.activeSlide.tween('left', this.changeLeft);

        this.effects.start(effect);
        this.currentIndex = this.nextIndex;
        this.changeBullet(this.currentIndex);   
    },
    autoSlide: function() {
        this.currentImage = this.imgs[this.currentIndex];
        this.controls[this.currentIndex].removeClass('active').addClass('inactive');
        this.nextIndex = (this.currentIndex<this.imgs.length-1)? (this.currentIndex+1): 0;
        this.nextImage = this.imgs[this.nextIndex];
        this.transition(this.currentImage, this.nextImage, false);
        
    },
    slideOnClick: function(index) {
        this.reset();
        this.timer = $clear(this.timer);
        this.nextIndex = index;
        this.currentImage = this.imgs[this.currentIndex];
        this.nextImage = this.imgs[this.nextIndex];
        this.transition(this.currentImage,this.nextImage,true); 
    },
    reset: function(){
        this.imgs.each(function(image,index){
            if(index!=this.currentIndex) {
                image.setStyle('margin-left',this.options.minMargin);
            }           
        }.bind(this));
    },
    changeBullet: function(active_index) {
        active_background = this.hidden_controls[0].getStyle('background');
        inactive_background = this.hidden_controls[1].getStyle('background');
        this.controls.each(function(cntrl, index){
            if(index == active_index) {
                cntrl.setStyle('background', active_background);
            } else {
                cntrl.setStyle('background', inactive_background);
            }
        }.bind(this));
    },
    setImgMargin: function() {
        this.imgs.each(function(img, index){
            if(index == 0) {
                img.setStyle('margin-left', this.options.startMargin);
            } else {
                img.setStyle('margin-left', this.options.maxMargin);
            }
        }.bind(this));
    }
});
window.addEvent('domready', function(){
    if ($('slideshow')) {
        if($$('.slide_banner').length > 0) {
            var slide = new ImageSlider($$('.slide_banner')[0]);
        }
    } 
});
