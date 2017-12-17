;(function(window) {

  var svgSprite = '<svg>' +
    '' +
    '<symbol id="icon-mima" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M510.293333 10.049255 510.293333 10.049255c74.782118 0 142.767686 30.579451 192.020078 79.811765 49.232314 49.242353 79.801725 117.227922 79.801725 192.030118l0 56.641255c-4.196392-0.532078-8.583529-0.863373-13.000784-0.863373L657.648941 337.66902l0-55.777882c0-40.377725-16.604863-77.251765-43.329255-103.966118-26.704314-26.724392-63.588392-43.329255-104.016314-43.329255l0 0c-40.468078 0-77.332078 16.604863-104.056471 43.329255-26.704314 26.714353-43.299137 63.588392-43.299137 103.966118l0 55.777882L254.84549 337.66902c-5.611922 0-11.093333 0.501961-16.494431 1.395451l0-57.163294c0-74.802196 30.58949-142.787765 79.841882-192.030118C367.48549 40.628706 435.471059 10.049255 510.293333 10.049255L510.293333 10.049255z"  ></path>' +
    '' +
    '<path d="M769.114353 368.790588 254.84549 368.790588c-54.292078 0-98.665412 44.433569-98.665412 98.665412l0 447.849412c0 54.201725 44.433569 98.635294 98.665412 98.635294l514.278902 0c54.272 0 98.705569-44.433569 98.705569-98.635294l0-447.849412C867.819922 413.224157 823.446588 368.790588 769.114353 368.790588zM598.27702 865.862275 435.722039 865.862275l33.119373-191.789176c-28.862745-17.02651-48.25851-48.449255-48.25851-84.399686 0-54.081255 43.801098-97.872314 97.882353-97.872314 54.041098 0 97.942588 43.791059 97.942588 97.872314 0 37.034667-20.590431 69.260549-50.959059 85.935686L598.27702 865.862275z"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '<symbol id="icon-telephone" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M183.872 103.68 103.424 184.576c-44.416 44.672-23.04 97.984 0 161.728 0 0 110.656 189.568 253.632 333.312 152.064 152.896 329.6 253.056 329.6 253.056 58.688 30.4 116.416 44.672 160.96 0L928 851.84c22.272-22.336 27.008-62.144 0-80.896l-160.896-121.344c-27.264-18.56-58.24-22.336-80.448 0l0 0 0 0-47.552 47.872c-55.808-41.856-117.888-92.864-173.696-148.928C416.128 498.944 372.288 445.184 335.808 395.84l49.216-49.472c22.208-22.336 18.432-53.44 0-80.896L264.32 103.68C242.112 81.344 206.08 81.344 183.872 103.68"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '<symbol id="icon-yanzhengma" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M889.064286 131.215484c-9.008164 0.323365-17.812691 0.445138-26.480094 0.445138-113.829512 0-195.830107-25.192775-249.467725-50.495044-53.650921-25.314549-78.952166-50.737568-79.371722-51.198056l-22.701025-24.00267-22.836101 24.00267c-0.907673 1.042749-99.215676 101.692077-328.758606 101.692077-8.68173 0-17.486256-0.121773-26.548656-0.445138l-31.965016-1.059122 0 456.946127c0 119.639844 41.352827 294.137087 398.892943 427.66115l11.146874 4.185322 11.161201-4.185322c357.526813-133.524063 398.87964-308.021306 398.87964-427.66115L921.015999 130.157385 889.064286 131.215484zM475.813335 705.309704l-205.988468-187.541327 54.721299-45.524846 109.523439 83.029018c0 0 151.212934-160.789033 297.266357-235.866962l20.871353 24.136723C752.207315 343.54231 569.692469 498.981499 475.813335 705.309704z"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '<symbol id="icon-name" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M742.08 731.648c-76.992-33.6-115.776-77.248-115.776-77.248-16.832-10.752-11.52-39.104-11.52-39.104 32.448-31.552 57.664-150.976 57.664-150.976 53.824-18.944 48.704-83.584 48.704-83.584 0-42.944-31.232-42.496-31.232-42.496 3.84-148.48 2.368-185.408-41.344-215.36C665.6 103.232 665.6 76.608 665.6 76.608S635.264 91.648 598.912 86.976C562.56 82.304 544.192 65.472 485.44 65.472c-42.624 0-87.296 14.592-89.344 57.856-67.2 11.776-76.928 92.16-62.08 214.848 0 0-31.232-0.512-31.232 42.496 0 0-5.12 64.64 48.704 83.584 0 0 25.28 119.424 57.728 150.976 0 0 5.312 28.352-11.456 39.104 0 0-38.784 43.648-115.776 77.248 0 0-188.352 70.592-188.352 153.088l0 73.792 836.928 0 0-73.792C930.432 802.176 742.08 731.648 742.08 731.648L742.08 731.648z"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '</svg>'
  var script = function() {
    var scripts = document.getElementsByTagName('script')
    return scripts[scripts.length - 1]
  }()
  var shouldInjectCss = script.getAttribute("data-injectcss")

  /**
   * document ready
   */
  var ready = function(fn) {
    if (document.addEventListener) {
      if (~["complete", "loaded", "interactive"].indexOf(document.readyState)) {
        setTimeout(fn, 0)
      } else {
        var loadFn = function() {
          document.removeEventListener("DOMContentLoaded", loadFn, false)
          fn()
        }
        document.addEventListener("DOMContentLoaded", loadFn, false)
      }
    } else if (document.attachEvent) {
      IEContentLoaded(window, fn)
    }

    function IEContentLoaded(w, fn) {
      var d = w.document,
        done = false,
        // only fire once
        init = function() {
          if (!done) {
            done = true
            fn()
          }
        }
        // polling for no errors
      var polling = function() {
        try {
          // throws errors until after ondocumentready
          d.documentElement.doScroll('left')
        } catch (e) {
          setTimeout(polling, 50)
          return
        }
        // no errors, fire

        init()
      };

      polling()
        // trying to always fire before onload
      d.onreadystatechange = function() {
        if (d.readyState == 'complete') {
          d.onreadystatechange = null
          init()
        }
      }
    }
  }

  /**
   * Insert el before target
   *
   * @param {Element} el
   * @param {Element} target
   */

  var before = function(el, target) {
    target.parentNode.insertBefore(el, target)
  }

  /**
   * Prepend el to target
   *
   * @param {Element} el
   * @param {Element} target
   */

  var prepend = function(el, target) {
    if (target.firstChild) {
      before(el, target.firstChild)
    } else {
      target.appendChild(el)
    }
  }

  function appendSvg() {
    var div, svg

    div = document.createElement('div')
    div.innerHTML = svgSprite
    svgSprite = null
    svg = div.getElementsByTagName('svg')[0]
    if (svg) {
      svg.setAttribute('aria-hidden', 'true')
      svg.style.position = 'absolute'
      svg.style.width = 0
      svg.style.height = 0
      svg.style.overflow = 'hidden'
      prepend(svg, document.body)
    }
  }

  if (shouldInjectCss && !window.__iconfont__svg__cssinject__) {
    window.__iconfont__svg__cssinject__ = true
    try {
      document.write("<style>.svgfont {display: inline-block;width: 1em;height: 1em;fill: currentColor;vertical-align: -0.1em;font-size:16px;}</style>");
    } catch (e) {
      console && console.log(e)
    }
  }

  ready(appendSvg)


})(window)