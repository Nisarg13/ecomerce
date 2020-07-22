;(function($) {

    "use strict";

    var $doc = $(document),
        $win = $(window),
        $body = $('body'),
        $header = $('header'),
        $cdNavicon = $('.cd-nav-icon'),
        $modal = $('#modal-login'),
        $loginModal = $('#login'),
        $rangeSlider = $('#slider-range'),
        $amount = $('#amount'),
        $amount1 = $('#amount1'),
        $amount2 = $('#amount2'),
        $quickView = $('#quick-view'),
        $accordion = $('#accordion'),
        $mainSlide = $('#banner-slider'),
        $mainBanner = $('.main-banner'),
        $modalTrigger = $('.trigger-modal'),
        $productSlide = $('.product-slide'),
        $instaSlide = $('.instaslide'),
        $thumbSlide = $('.thumb-slider'),
        $thumbSlideModal = $('.thumb-slider-modal'),
        $countWrap = $('.cont-wrap'),
        $flashCount = $('.flash-count'),
        $scrollUp = $('.scrollup'),
        $add = $('.add'),
        $minus = $('.minus'),
        $group1 = $('.group1'),
        $gridWrap = $('.grid-wrap'),
        $grid = $('.grid'),
        $featurePostList = $('.feature-post-list'),
        $absoluteWrap = $('.absolute-wrap'),
        $supportAccordion = $('.support-accordion'),
        $navTigger = $('.cd-nav-trigger'),
        $dlMenu = $('#dl-menu'),
        $newsletter = $('#newsletter'),
        $cdNavWrap = $('.cd-navigation-wrapper'),
        $carousel = $('.carousel');

    // normal JS selector
    var newEl;

    // bxSliders
    var bxSlider1, bxSlider2, bxSlider3, bxSlider4;

    //thumb slider
    var thumbSlider = {
        pagerCustom: '#thumb-pager',
        auto: true,
        controls: false
    };

    // feature post list
    var featurePostList = {
        auto: true,
        controls: false,
        pager: true,
    };

    /**
     * Parameters for Product Slide
     */
    function getProductSlideParams() {
        var params;
        // get the window width
        var winWidth = $win.width();

        if (winWidth < 767) {
            params = {
                auto: true,
                minSlides: 1,
                maxSlides: 1,
                slideMargin: 0,
                controls: false,
                moveSlides: 4
            };
        } else if (winWidth < 991) {
            params = {
                auto: true,
                minSlides: 2,
                maxSlides: 2,
                slideMargin: 30,
                slideWidth: 350,
                controls: false,
                moveSlides: 2
            };
        } else {
            params = {
                auto: true,
                minSlides: 4,
                maxSlides: 4,
                slideWidth: 270,
                slideMargin: 30,
                moveSlides: 4,
                controls: false,
                pager: true
            };
        }

        return params;
    }

    /**
     * Parameters for Instagram Slider
     */
    function getInstagramSliderParams() {
        var params;
        // get the window width
        var winWidth = $win.width();
        params = {
            auto: true,
            minSlides: 4,
            maxSlides: 8,
            slideWidth: 270,
            slideMargin: 30,
            moveSlides: 4,
            controls: true,
            pager: false,
            nextText: '<i class=" fa fa-angle-right"></i>',
            prevText: '<i class=" fa fa-angle-left"></i>'
        };
        return params;
    } 

    // responsive menu
    if($(window).width()<768){
        $('.navbar-nav>li.dropdown>a').on('click',function(event){
            event.preventDefault();
            $(this).next().slideToggle();
        });
    }

    /**
     * Initialize the bxSlider
     * 
     * @param selector
     * @param bxSlider objects
     */
    function initBxSlider($el, params) {
        return $el.bxSlider(params);
    }

    /**
     * Reload BxSlider
     * @param {*} sliderObj BxSlider Object
     * @param {*} params 
     */
    function reloadBxSlider(sliderObj, params) {
        return sliderObj.reloadSlider(params);
    }


    /**
     * Modal
     * Toggles between login, register & forgot password
     * with the same instance without actually loading for 3 modals
     */
    $modalTrigger.on('click', function(e) {
        event.preventDefault();
        var isModal = false;
        var currentEl = e.currentTarget;
        var target = $(currentEl).data('show');
        var $el = $(this);

        if (!isModal) {
            $modal.modal('show');
            $(newEl).addClass('hidden');
            $(target).removeClass('hidden');
            newEl = '';
            isModal = false;
        }
        newEl = target;

        // after the modal is displayed
        $modal.on('shown.bs.modal', function() {
            isModal = true;
            newEl = target;
            $(target).removeClass('hidden');
        });

        // before actually hiding the modal
        $modal.on('hide.bs.modal', function() {
            target = '';
            isModal = false;
            $(newEl).removeClass('hidden');
            $modal.find('.modal-dialog').children('div').addClass('hidden');
        });

    });

    /**
     * END Login, Register & Forgot Password Modal 
     */

    //set screen height
    function setHeight() {
        var windowHeight = $win.innerHeight();
        $absoluteWrap.css('height', windowHeight + "px");
    }

    function init() {
        setHeight(); 

        $carousel.carousel({
             interval: 5000,
             pause: "false"
        });

        /**
         * BxSliders
         */
        var productSlideparams = getProductSlideParams();
        var instaSliderParams = getInstagramSliderParams();

        bxSlider1 = initBxSlider($productSlide, productSlideparams);
        bxSlider2 = initBxSlider($instaSlide, instaSliderParams);
        bxSlider3 = initBxSlider($thumbSlide, thumbSlider);
        bxSlider4 = initBxSlider($featurePostList, featurePostList);

    }
    init();

    /**
     * When the window resizes
     */
    $win.bind('resize', function(e) {
        window.resizeEvt;
        $win.resize(function() {
            clearTimeout(window.resizeEvt);
            window.resizeEvt = setTimeout(function() {
                var productSlideparams = getProductSlideParams();
                var instaSliderParams = getInstagramSliderParams();
                
                reloadBxSlider(bxSlider1, productSlideparams);
                reloadBxSlider(bxSlider2, instaSliderParams);

                setHeight();
            }, 250);
        });
    });


    /**
     * WOW animation
     */
    var wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 100,
    });
    wow.init();
    /**
     * END WOW animation
     */

    //price range
    $rangeSlider.slider({
        range: true,
        min: 0,
        max: 10000,
        values: [0, 10000],
        slide: function(event, ui) {
            $amount.html("Rs" + ui.values[0] + " - Rs" + ui.values[1]);
            $amount1.val(ui.values[0]);
            $amount2.val(ui.values[1]);
        }
    });

    $amount.html("Rs" + $rangeSlider.slider("values", 0) +
        " - Rs" + $rangeSlider.slider("values", 1));

        $('#multi').mdbRange({
            single: {
              active: true,
              multi: {
                active: true,
                rangeLength: 1
              },
            }
          });

    //Quickview modal
    $quickView.on('shown.bs.modal', function(e) {
        $thumbSlideModal.bxSlider({
            pagerCustom: '#thumb-pager',
            auto: true,
            controls: false
        });
    });

    //increase quantity
    $add.on('click', function() {
        var $qty = $(this).closest('div').find('.qty');
        var currentVal = parseInt($qty.val());
        if (!isNaN(currentVal)) {
            $qty.val(currentVal + 1);
        }
    });

    //decrease quantity
    $minus.on('click', function() {
        var $qty = $(this).closest('div').find('.qty');
        var currentVal = parseInt($qty.val());
        if (!isNaN(currentVal) && currentVal > 0) {
            $qty.val(currentVal - 1);
        }
    });

    //support accordion 
    $supportAccordion.accordion({
        heightStyle: "content"
    });

    //light box
    $group1.colorbox({
        rel: 'group1'
    });

    //count down
    if ($countWrap.length) {
        var endDate = new Date($countWrap.data("end-date"));
        $countWrap.countdown({
            date: endDate,
            render: function(data) {
                $(this.el).html(
                    '<div><span class="no rounded-crcl">' + this.leadingZeros(data.days, 2) + '</span> DAYS</div>' +
                    '<div><span class="no rounded-crcl">' + this.leadingZeros(data.hours, 2) + '</span> HOURS</div>' +
                    '<div><span class="no rounded-crcl">' + this.leadingZeros(data.min, 2) + '</span> MINUTES</div>' +
                    '<div><span class="no rounded-crcl">' + this.leadingZeros(data.sec, 2) + '</span> SEC</div>'
                );
            }
        });
    }

    //count down
    if ($flashCount.length) {
        var endDate = new Date($flashCount.data("end-date"));
        $flashCount.countdown({
            date: endDate,
            render: function(data) {
                $(this.el).html( 
                    '<div>' + this.leadingZeros(data.hours, 2) + ' </div>' +
                    '<div>' + this.leadingZeros(data.min, 2) + ' </div>' +
                    '<div>' + this.leadingZeros(data.sec, 2) + ' </div>'
                );
            }
        });
    }



    //Back to top
    $win.on('scroll', function() {
        // shrink the navbar
        if ($(this).scrollTop() > 700) { //Adjust 150
            $header.addClass('shrinked');
            $cdNavicon.addClass('icon-blk');
        } else {
            $header.removeClass('shrinked');
            $cdNavicon.removeClass('icon-blk');
        }

        // toggles the display of scroll to top button
        if ($(this).scrollTop() > 400) {
            $scrollUp.fadeIn();
        } else {
            $scrollUp.fadeOut();
        }

    });

    // scroll to top
    $scrollUp.on("click", function() {
        $("html, body").animate({
            scrollTop: 0
        }, 1500);
        return false;
    });

    // expandable search form
    var submitIcon = $('.searchbox-icon');
    var inputBox = $('.searchbox-input');
    var searchBox = $('.searchbox');
    var isOpen = false;

    submitIcon.on('click',function() {
        if (isOpen == false) {
            searchBox.addClass('searchbox-open');
            inputBox.focus();
            isOpen = true;
        } else {
            searchBox.removeClass('searchbox-open');
            inputBox.focusout();
            isOpen = false;
        }
    });

    submitIcon.on('mouseup',function() {
        return false;
    });

    searchBox.on('mouseup', function() {
        return false;
    });

    $win.on('mouseup',function() {
        if (isOpen == true) {
            submitIcon.css('display', 'block');
            submitIcon.click();
        }
    });


    function buttonUp() {
        var inputVal = inputBox.val();
        inputVal = $.trim(inputVal).length;
        if (inputVal !== 0) {
            submitIcon.css('display', 'none');
        } else {
            inputBox.val('');
            submitIcon.css('display', 'block');
        }
    }

    //product description accordion 
    $accordion.accordion({
        heightStyle: "content"
    });

    // Initialize masonry after everything is loaded 
    $win.on('load', function(e){
        // masonry

        $grid.masonry({
            itemSelector: '.grid-item'
        });

        //culture masonary 
        $gridWrap.masonry({
            itemSelector: '.item'
        });
    });

    $dlMenu.dlmenu({
        animationClasses: { in: 'dl-animate-in-2', out: 'dl-animate-out-2' }
    });


    //open/close lateral navigation
    var isLateralNavAnimating = false;

    $navTigger.on('click', function(event) {
        event.preventDefault();
        //stop if nav animation is running 
        if (!isLateralNavAnimating) {
            if ($(this).parents('.csstransitions').length > 0) isLateralNavAnimating = true;

            $body.toggleClass('navigation-is-open');
            $cdNavWrap.one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
                //animation is over
                isLateralNavAnimating = false;
            });
        }
    });

    // newletter
    $newsletter.modal('show')

})(jQuery);