$(document).ready(function () {
    $(document).on('click', '.express-button', function () {
        const content = `
            <form class="express-popup">
                <figure class="express-button">
                    <img src="images/express_button.png" alt="Express button icon">
                </figure>
                <div class="express-input-area">
                    <input type="text" placeholder="express...">
                    <div>
                        <svg
                        id="emojiIcon"
                        width="18"
                        height="18"
                        viewBox="0 0 22 22"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                        >
                        <g clip-path="url(#clip0_66_2023)">
                        <path
                            d="M20.1662 10.0835V11.0002C20.157 12.8503 19.5881 14.6544 18.5343 16.1751C17.4806 17.6959 15.9913 18.8621 14.2623 19.5207C12.5333 20.1792 10.6455 20.2991 8.84711 19.8646C7.04869 19.4302 5.42384 18.4617 4.18615 17.0864C2.94847 15.7112 2.15589 13.9937 1.91261 12.1596C1.66933 10.3255 1.98674 8.46075 2.82311 6.81043C3.65948 5.16012 4.97566 3.80151 6.59862 2.91322C8.22158 2.02494 10.0754 1.64855 11.9162 1.83354"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        <path
                            d="M7.33301 12.8335C7.33301 12.8335 8.70801 14.6668 10.9997 14.6668C13.2913 14.6668 14.6663 12.8335 14.6663 12.8335"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        <path
                            d="M8.25 8.25H8.25875"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        <path
                            d="M13.75 8.25H13.7588"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        <path
                            d="M14.667 4.5835H20.167"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        <path
                            d="M17.417 1.8335V7.3335"
                            stroke="black"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                        </g>
                        <defs>
                        <clipPath id="clip0_66_2023">
                            <rect width="22" height="22" fill="white" />
                        </clipPath>
                        </defs>
                    </svg>
                    <svg
                        id="imageIcon"
                        width="16"
                        height="16"
                        viewBox="0 0 20 20"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                        >
                        <path
                        d="M17 1H3C1.89543 1 1 1.89543 1 3V17C1 18.1046 1.89543 19 3 19H17C18.1046 19 19 18.1046 19 17V3C19 1.89543 18.1046 1 17 1Z"
                        stroke="black"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        />
                        <path
                        d="M6.5 8C7.32843 8 8 7.32843 8 6.5C8 5.67157 7.32843 5 6.5 5C5.67157 5 5 5.67157 5 6.5C5 7.32843 5.67157 8 6.5 8Z"
                        stroke="black"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        />
                        <path
                        d="M19 13L14 8L3 19"
                        stroke="black"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        />
                    </svg>
                    </div>
                </div>
                <svg
                id="submitButton"
                width="16"
                height="16"
                viewBox="0 0 20 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    d="M19 13V17C19 17.5304 18.7893 18.0391 18.4142 18.4142C18.0391 18.7893 17.5304 19 17 19H3C2.46957 19 1.96086 18.7893 1.58579 18.4142C1.21071 18.0391 1 17.5304 1 17V13"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                />
                <path
                    d="M15 6L10 1L5 6"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                />
                <path
                    d="M10 1V13"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                />
                </svg>
            </form>
        `;
        const expressPopup = $(content);
        const expressButton = $(this);

        expressButton.replaceWith(expressPopup);
        expressPopup.fadeIn();

        expressPopup.find('.express-button').css({
            'margin-top': '0px',
        });

        expressPopup.find('img').css('cursor', 'auto');

        expressPopup.on('click', function(event) {
            event.stopPropagation();
        });

        function handleMouseup(e) {
            if (!expressPopup.is(e.target) && expressPopup.has(e.target).length === 0) {
                expressPopup.fadeOut(function () {
                    expressButton.insertAfter(expressPopup);
                    $(document).off('mouseup', handleMouseup);
                });
            }
        }

        $(document).on('mouseup', handleMouseup);
    });   
});
