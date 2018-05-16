define(["require","exports","tslib","external/keymaster","external/react","external/classnames","jquery","modules/clean/analytics","modules/clean/keycode","modules/clean/react/css_timing","modules/clean/react/file_viewer/actions","modules/clean/previews/util","modules/clean/react/file_viewer/constants","modules/clean/react/file_viewer/full_screen_helpers","modules/clean/react/file_viewer/sidebar_helpers","modules/clean/react/keyboard_binding/keyboard_binding_connector","modules/clean/react/previews/frame_messenger_host","modules/clean/react/size_class/constants","modules/clean/react/sprite","modules/clean/static_urls","modules/core/dom","modules/core/exception","modules/core/i18n"],function(e,t,o,n,r,i,s,a,l,c,p,u,d,m,y,g,h,f,b,C,w,P,T){"use strict";function _(e){var t=e.className,o=e.disabled,n=e.iconName,s=e.onClick,a=e.spriteGroup,l=e.spriteName,c=e.tooltip;return r.createElement("div",{className:i(t,"toolbar-button-entry"),onMouseUp:s},r.createElement("div",{className:"toolbar-tooltip"},r.createElement("div",{className:"toolbar-tooltip-container"},r.createElement("div",{className:"toolbar-tooltip-pointer-border"})),r.createElement("div",{className:"toolbar-tooltip-container"},r.createElement("div",{className:"toolbar-tooltip-body"},c)),r.createElement("div",{className:"toolbar-tooltip-container"},r.createElement("div",{className:"toolbar-tooltip-pointer"}))),r.createElement("button",{alt:c},void 0!==n?r.createElement("img",{src:C.static_url("/static/images/previews/toolbar/"+n+".svg"),alt:c,className:i({disabled:o})}):r.createElement(b.Sprite,{group:a,name:l,alt:c,className:i({disabled:o})})))}function v(e){var t=e.currentPage,o=e.docType,n=e.pagesCount,i=e.sizeClass;if(!t||!n)return null;var s="";s=i===f.SizeClass.Small?T._("%(current_page)s of %(pages_count)s"):o===d.DocType.ppt?T._("Slide %(current_page)s of %(pages_count)s"):T._("Page %(current_page)s of %(pages_count)s");var a=s.format({current_page:t,pages_count:n});return r.createElement("div",{className:E.PAGE_INDICATOR},a)}Object.defineProperty(t,"__esModule",{value:!0});var K={};K[l.KeyCode.ESC]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.SPACE]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.PAGE_UP]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.PAGE_DOWN]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.LEFT]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.UP]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.RIGHT]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.DOWN]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.EQUALS]={altKey:!0,ctrlKey:!0,metaKey:!0},K[70]={altKey:!1,ctrlKey:!0,metaKey:!0},K[80]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.PLUS_EQUALS_FF]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.MINUS_FF]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.PLUS_EQUALS_FF_GERMAN]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.MINUS_FF_MAC]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.PLUS_CHROME]={altKey:!0,ctrlKey:!0,metaKey:!0},K[l.KeyCode.MINUS_CHROME]={altKey:!0,ctrlKey:!0,metaKey:!0};var S,E={ENABLE_REGION_CREATION:"enable-region-creation",FULLSCREEN:"fullscreen",PAGE_DOWN:"page-down",PAGE_INDICATOR:"page-indicator",PAGE_UP:"page-up",PRINT:"print",SIDEBAR:"sidebar",ZOOM_IN:"zoom-in",ZOOM_OUT:"zoom-out"};(function(e){e[e.EnableRegionCreation=0]="EnableRegionCreation",e[e.Fullscreen=1]="Fullscreen",e[e.PageDown=2]="PageDown",e[e.PageIndicator=3]="PageIndicator",e[e.PageUp=4]="PageUp",e[e.Print=5]="Print",e[e.Sidebar=6]="Sidebar",e[e.ZoomIn=7]="ZoomIn",e[e.ZoomOut=8]="ZoomOut"})(S||(S={}));var M,O=(D={},D[d.DocType.default]=[],D[d.DocType.pdf]=[S.Sidebar,S.PageIndicator,S.ZoomIn,S.ZoomOut,S.PageUp,S.PageDown,S.Fullscreen,S.Print,S.EnableRegionCreation],D[d.DocType.ppt]=[S.Sidebar,S.PageIndicator,S.PageUp,S.PageDown,S.Fullscreen,S.Print,S.EnableRegionCreation],D[d.DocType.spreadsheet]=[S.ZoomIn,S.ZoomOut,S.Fullscreen,S.Print],D[d.DocType.html]=[S.Fullscreen,S.Print],D),N=(I={},I[d.DocType.default]=[],I[d.DocType.pdf]=[S.PageIndicator],I[d.DocType.ppt]=[S.PageIndicator],I[d.DocType.spreadsheet]=[],I[d.DocType.html]=[],I);(function(e){e.ClearMouseTracking="clear-mouse-tracking",e.EnableRegionCreation="enable-region-creation",e.EnterFullscreen="enter-fullscreen",e.ExitViewerFullscreen="exit-viewer-fullscreen",e.PageDown="page-down",e.PageUp="page-up",e.PreviewToolbarMounted="preview-toolbar-mounted",e.Print="print",e.ScreenDown="screen-down",e.ScreenUp="screen-up",e.ScrollDown="scroll-down",e.ScrollLeft="scroll-left",e.ScrollRight="scroll-right",e.ScrollUp="scroll-up",e.ZoomIn="zoom-in",e.ZoomOut="zoom-out"})(M||(M={}));t.PreviewToolbarButton=_;var F=(function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.handleClick=function(){var e=t.props,o=e.isSidebarOpen,n=e.onClick,r=e.onSidebarClose,i=e.onSidebarOpen;o&&r?r():i&&i(),n&&n()},t}return o.__extends(t,e),t.prototype.render=function(){var e=this.props,t=e.disabled,o=e.isSidebarOpen;return r.createElement(_,{className:E.SIDEBAR,disabled:t,iconName:o?"sidebar_hide":"sidebar_show",tooltip:o?T._("Hide sidebar"):T._("Show sidebar"),onClick:this.handleClick})},t})(r.PureComponent),U=(function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.previewOpen=!1,t.state={currentPage:1,visible:!1,fadingOut:!1,disabledButtons:{}},t.handleMessageFromChild=function(e){var o={input_method:"child-message",file_ext:t.props.fileExtension},n={context:d.UserActionContext.Unknown};switch(e.action){case"page-change":var r=e.parameters,i=t.isToolbarReadyToShow(),s=t.sanitizePageNumber(r.current_page),l=t.sanitizePageNumber(t.props.pagesCount||r.pages_count);if(s<=0||l<=0)break;var c={pageUp:s<=1,pageDown:s>=l,print:!t.canPrint()};t.setState({currentPage:s,disabledButtons:c},function(){!i&&t.isToolbarReadyToShow()&&(t.fadeIn(),t.startIdleTimeout())});break;case"idle-mouse":t.state.hovering||t.fadeOut(),a.PreviewActivityLogger.log("idle-mouse",o);break;case"active-mouse":t.fadeIn();break;case"exit-parent-fullscreen":t.setFullScreen(!1,n);break;case"keydown":t.onKeydown(e.parameters);break;case"get-keydown-keys-handled-by-parent":t.postKeysHandledByParent()}},t.onSidebarClose=function(){"function"==typeof t.props.onSidebarClose&&t.props.onSidebarClose(d.UserActionContext.Toolbar)},t.onSidebarOpen=function(){"function"==typeof t.props.onSidebarOpen&&t.props.onSidebarOpen(d.UserActionContext.Toolbar)},t.onMouseEnterToolbar=function(){t.frameMessenger.postMessageToChildren(M.ClearMouseTracking),t.setState({hovering:!0}),t.clearIdleTimeout()},t.onMouseLeaveToolbar=function(){t.setState({hovering:!1})},t.onKeydown=function(e){var o=!1;if(t.frameMessenger.childIsValidated()&&"dbmodal"!==n.getScope()&&!w.focus_in_input()&&!w.is_input(e.target)){if(null!=e.target){var r=s("#file-comments");if(1!==r.length&&(r=s("#photo-comments")),1===r.length&&(e.target===r[0]||s.contains(r[0],e.currentTarget)))return}var i={input_method:"keydown",file_ext:t.props.fileExtension,extra:JSON.stringify({keycode:e.keyCode})},a={context:d.UserActionContext.Keyboard},c=e.keyCode;return t.props.docType!==d.DocType.ppt&&[l.KeyCode.EQUALS,l.KeyCode.PLUS_EQUALS_FF,l.KeyCode.PLUS_CHROME,l.KeyCode.PLUS_EQUALS_FF_GERMAN].indexOf(c)>-1?(t.zoomIn(a),o=!0):t.props.docType!==d.DocType.ppt&&[l.KeyCode.MINUS_FF_MAC,l.KeyCode.MINUS_FF,l.KeyCode.MINUS_CHROME].indexOf(c)>-1?(t.zoomOut(a),o=!0):c===l.KeyCode.LEFT?(t.scrollLeft(i),o=!0):c===l.KeyCode.RIGHT?(t.scrollRight(i),o=!0):c===l.KeyCode.PAGE_UP?(t.props.docType===d.DocType.ppt?t.pageUp(i):t.screenUp(i),o=!0):[l.KeyCode.SPACE,l.KeyCode.PAGE_DOWN].indexOf(c)>-1?(t.props.docType===d.DocType.ppt?t.pageDown(i):t.screenDown(i),o=!0):c===l.KeyCode.UP?(t.props.docType===d.DocType.ppt?t.pageUp(i):t.scrollUp(i),o=!0):c===l.KeyCode.DOWN?(t.props.docType===d.DocType.ppt?t.pageDown(i):t.scrollDown(i),o=!0):70!==c||e.ctrlKey||e.metaKey?70===c&&(e.ctrlKey||e.metaKey)?t.searchInline(a):80===c?(t.printDocument(a),o=!0):c===l.KeyCode.ESC&&(t.isViewerFullscreen()?t.exitFullscreen(a):t.props.afterFileViewerExit&&!t.isAnnotationBubbleShown()&&t.exitPreview(i),o=!0):(t.isViewerFullscreen()?t.exitFullscreen(a):t.enterFullscreen(a),o=!0),o&&null!=e.preventDefault&&e.preventDefault(),!o}},t.onIdleTimeout=function(){t.clearIdleTimeout(),t.fadeOut()},t.pageUp=function(e){t.logAndPostMessage(M.PageUp,"page-up",e)},t.pageDown=function(e){t.logAndPostMessage(M.PageDown,"page-down",e)},t.screenUp=function(e){t.logAndPostMessage(M.ScreenUp,"screen-up",e)},t.screenDown=function(e){t.logAndPostMessage(M.ScreenDown,"screen-down",e)},t.scrollUp=function(e){t.logAndPostMessage(M.ScrollUp,"scroll-up",e)},t.scrollDown=function(e){t.logAndPostMessage(M.ScrollDown,"scroll-down",e)},t.scrollRight=function(e){t.logAndPostMessage(M.ScrollRight,"scroll-right",e)},t.scrollLeft=function(e){t.logAndPostMessage(M.ScrollLeft,"scroll-left",e)},t}return o.__extends(t,e),t.prototype.reset=function(){this.clearAllTimeouts(),this.setState({currentPage:0,visible:!1,fadingOut:!1,disabledButtons:{}})},t.prototype.setFullScreen=function(e,t){e?m.enterFullScreen(!0,t.context):m.exitFullScreen(t.context)},t.prototype.isViewerFullscreen=function(){return this.props.isFullscreen||m.isBrowserFullscreen()},t.prototype.postKeysHandledByParent=function(){this.frameMessenger.postMessageToChildren("keydown-keys-handled-by-parent",{keycodes:K})},t.prototype.onPreviewOpen=function(){return!!this.previewOpen||(s(document).on("keydown",this.onKeydown),this.previewOpen=!0,!0)},t.prototype.onPreviewClose=function(){return!this.previewOpen||(s(document).off("keydown",this.onKeydown),this.reset(),this.frameMessenger.resetOriginsForPosting(),this.previewOpen=!1,!0)},t.prototype.componentDidMount=function(){this.props.frameMessenger?this.frameMessenger=this.props.frameMessenger:this.frameMessenger=new h.PreviewFrameMessengerHost,this.frameMessenger.configureChildMessaging(u.getIframeQuery(),this.handleMessageFromChild,["page-change","idle-mouse","active-mouse","exit-parent-fullscreen","keydown","child-focus","get-keydown-keys-handled-by-parent"]),this.frameMessenger.startListening(),this.postKeysHandledByParent(),this.onPreviewOpen(),this.frameMessenger.postMessageToChildren(M.PreviewToolbarMounted),this.fadeIn(),this.startIdleTimeout()},t.prototype.componentWillUnmount=function(){this.clearAllTimeouts(),this.onPreviewClose(),this.frameMessenger.stopListening()},t.prototype.canPrint=function(){return!(this.props.sharePermissions&&this.props.sharePermissions.canPrintRoles&&0===this.props.sharePermissions.canPrintRoles.length)},t.prototype.showButton=function(e){var t=this.props.sizeClass===f.SizeClass.Small?N[this.props.docType]:O[this.props.docType];return Array.isArray(t)&&t.includes(e)},t.prototype.render=function(){var e,t=this,o=this.props,n=o.docType,s=o.fileExtension,a=o.isArchiveFile,l=o.isFullscreen,c=o.isHidden,p=o.isSidebarOpen,u=o.pagesCount,m=o.shouldDisplayRegionCreationButton,h=o.sizeClass,f=n===d.DocType.ppt?T._("Previous slide"):T._("Page up"),b=n===d.DocType.ppt?T._("Next slide"):T._("Page down");e=this.canPrint()?T._("Print"):T._("Printing is turned off for this file.");var C={input_method:"click",file_ext:s},w={context:d.UserActionContext.Toolbar},P=function(e){return function(){e(),t.frameMessenger.postMessageToChildren(M.ClearMouseTracking)}};return r.createElement("div",{className:i("preview-toolbar-overlay-container",{hide:!this.state.visible||c,fadeout:this.state.fadingOut})},r.createElement(g.KeyboardBindingConnector,{allKeyCallback:this.onKeydown}),r.createElement("div",{className:"preview-toolbar-overlay",onMouseEnter:this.onMouseEnterToolbar,onMouseLeave:this.onMouseLeaveToolbar},r.createElement("div",{className:"preview-toolbar-content"},this.showButton(S.Sidebar)&&y.isSidebarEnabled(n,h,l)?r.createElement(F,{isSidebarOpen:p,onSidebarClose:this.onSidebarClose,onSidebarOpen:this.onSidebarOpen}):null,this.showButton(S.PageIndicator)?r.createElement(v,{currentPage:this.state.currentPage,docType:n,pagesCount:u,sizeClass:h}):null,this.showButton(S.ZoomOut)?r.createElement(_,{className:E.ZOOM_OUT,spriteGroup:"web",spriteName:"zoomout",tooltip:T._("Zoom out"),onClick:P(function(){return t.zoomOut(w)})}):null,this.showButton(S.ZoomIn)?r.createElement(_,{className:E.ZOOM_IN,spriteGroup:"web",spriteName:"zoom",tooltip:T._("Zoom in"),onClick:P(function(){return t.zoomIn(w)})}):null,this.showButton(S.PageUp)?r.createElement(_,{disabled:this.state.disabledButtons.pageUp,className:E.PAGE_UP,spriteGroup:"web",spriteName:"up",tooltip:f,onClick:P(function(){return t.pageUp(C)})}):null,this.showButton(S.PageDown)?r.createElement(_,{disabled:this.state.disabledButtons.pageDown,className:E.PAGE_DOWN,spriteGroup:"web",spriteName:"down",tooltip:b,onClick:P(function(){return t.pageDown(C)})}):null,this.showButton(S.Fullscreen)?r.createElement(_,{className:E.FULLSCREEN,spriteGroup:"web",spriteName:"fullscreen",tooltip:T._("Fullscreen"),onClick:P(function(){return t.toggleFullscreen(w)})}):null,this.showButton(S.Print)&&!a?r.createElement(_,{disabled:!this.canPrint(),className:E.PRINT,spriteGroup:"web",spriteName:"print",tooltip:e,onClick:this.canPrint()?P(function(){return t.printDocument(w)}):function(){}}):null,this.showButton(S.EnableRegionCreation)&&m?r.createElement(_,{className:E.ENABLE_REGION_CREATION,spriteGroup:"web",spriteName:"ic_comment_area_large",tooltip:T._("Comment on specific areas"),onClick:P(function(){return t.onRegionCreationClick()})}):null)))},t.prototype.sanitizePageNumber=function(e){return null==e?0:isNaN(e)?0:e},t.prototype.fadeOut=function(){this.state.fadingOut||this.clearFadeTimeout(),this.setState({fadingOut:!0,tooltipClass:void 0}),this.props.onToolbarHide&&this.props.onToolbarHide(),this.startFadeTimeout()},t.prototype.fadeIn=function(){this.clearIdleTimeout(),this.isViewerFullscreen()||this.isToolbarReadyToShow()&&(this.clearFadeTimeout(),this.setState({visible:!0,fadingOut:!1}),this.props.onToolbarShow&&this.props.onToolbarShow())},t.prototype.isAnnotationBubbleShown=function(){return s(".annotation-bubble-container .bubble-dropdown").length>0},t.prototype.startFadeTimeout=function(){var e=this;this.fadeTimeout=setTimeout(function(){e.fadeTimeout=void 0,e.setState({visible:!1,fadingOut:!1})},400)},t.prototype.clearFadeTimeout=function(){this.fadeTimeout&&(clearTimeout(this.fadeTimeout),this.fadeTimeout=void 0)},t.prototype.startIdleTimeout=function(){this.clearIdleTimeout(),this.idleTimeout=setTimeout(this.onIdleTimeout,1500)},t.prototype.clearIdleTimeout=function(){null!=this.idleTimeout&&(clearTimeout(this.idleTimeout),this.idleTimeout=void 0)},t.prototype.clearAllTimeouts=function(){this.clearFadeTimeout(),this.clearIdleTimeout()},t.prototype.isToolbarReadyToShow=function(){return!!this.state.currentPage&&!!this.props.pagesCount},t.prototype.logData=function(e,t){return"string"==typeof t.input_method?a.PreviewActivityLogger.log(e,t):P.assert(!1,"logData not correctly formed"),"string"==typeof t.input_method},t.prototype.logUserAction=function(e,t){p.logUserAction(e,t)},t.prototype.logAndPostMessage=function(e,t,o){this.logData(t,o)&&this.frameMessenger.postMessageToChildren(e)},t.prototype.zoomIn=function(e){this.frameMessenger.postMessageToChildren(M.ZoomIn),this.logUserAction(d.UserAction.ZoomIn,e.context)},t.prototype.zoomOut=function(e){this.frameMessenger.postMessageToChildren(M.ZoomOut),this.logUserAction(d.UserAction.ZoomOut,e.context)},t.prototype.toggleFullscreen=function(e){this.isViewerFullscreen()?this.exitFullscreen(e):this.enterFullscreen(e)},t.prototype.enterFullscreen=function(e){this.setFullScreen(!0,e)},t.prototype.exitFullscreen=function(e){this.setFullScreen(!1,e)},t.prototype.exitPreview=function(e){if(this.logData("exit-preview",e))return"function"==typeof this.props.afterFileViewerExit?this.props.afterFileViewerExit():void 0},t.prototype.printDocument=function(e){this.frameMessenger.postMessageToChildren(M.Print,{context:e.context})},t.prototype.searchInline=function(e){this.logUserAction(d.UserAction.InlineSearch,e.context)},t.prototype.onRegionCreationClick=function(){this.props.onRegionCreationClick&&this.props.onRegionCreationClick()},t.defaultProps={docType:d.DocType.default},t})(r.Component);t._PreviewToolbar=U;var A=c.requireCssWithComponent(U,["/static/css/preview_toolbar-vfljuRcPV.css"]);t.PreviewToolbar=A,t.PageIndicator=v;var D,I});
//# sourceMappingURL=preview_toolbar.min.js-vflJkYLkt.map