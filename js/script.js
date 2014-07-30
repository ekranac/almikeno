$(document).ready(function(){
    $(".post-button").mouseenter(function(){
        $(this).stop().fadeTo(150,0.7)
    })
    $(".post-button").mouseleave(function(){
        $(this).stop().fadeTo(150, 1)
    })

    $(".navbar-right > li").click(function(){
        alert("Nothing yet, firbec :D")
    })
})

$(document).ready(function(){
    $(".post-image-button").click(function(){
        window.scrollTo(0,0)
        $(".text-post-title").val("")
        $(".text-post-content").val("")

        $(".new-text-post-container").fadeOut(function(){
            $(".new-image-post-container").fadeIn()
        })
    })
    
    $(".post-text-button").click(function(){
        window.scrollTo(0,0)
        $(".image-post-title").val("")
        $(".image-post-url").val("")

        $(".new-image-post-container").fadeOut(function(){
            $(".new-text-post-container").fadeIn()
        })
    })
})