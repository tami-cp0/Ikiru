$(document).ready(function () {
    $(document).on('click', '.express-button', function () {
        const content = `
            <form class="express-popup">
                <div class="express-switch-buttons-container">
                    <div class="emoji-image-container">
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
                    <div class="switch-button">
                        <p>Public</p>
                        <svg class="switch-icon" width="15" height="15" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_370_1233)">
                        <path d="M13.458 0.791504L16.6247 3.95817L13.458 7.12484" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M2.375 8.7085V7.12516C2.375 6.28531 2.70863 5.47986 3.3025 4.88599C3.89636 4.29213 4.70181 3.9585 5.54167 3.9585H16.625" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M5.54167 18.2083L2.375 15.0417L5.54167 11.875" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M16.625 10.2915V11.8748C16.625 12.7147 16.2914 13.5201 15.6975 14.114C15.1036 14.7079 14.2982 15.0415 13.4583 15.0415H2.375" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </g>
                        <defs>
                        <clipPath id="clip0_370_1233">
                        <rect width="19" height="19" fill="white"/>
                        </clipPath>
                        </defs>
                        </svg>
                    </div>
                    <figure class="express-button2">
                        <img src="images/express_button.png" alt="Express button icon">
                    </figure>
                </div>
                <div class="express-input-area">
                    <textarea placeholder="express..." maxlength="256"></textarea>
                </div>
                <div class="counter-post">
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
                    <div class="counter">0/256</div>
                </div>
            </form>
        `;
        const expressPopup = $(content);
        const expressButton = $(this);

        expressButton.replaceWith(expressPopup);
        expressPopup.fadeIn();

        expressPopup.find('.express-button2').css({
            'margin-top': '0px',
        });

        $('.darkmode-icon').attr('style','margin-top:14px');

        const darkMode = document.getElementsByClassName('darkmode-icon')[0];
        if (window.innerHeight > 768) {
            darkMode.classList.add('darkmode-icon2');
        } else {
            darkMode.classList.remove('darkmode-icon2');
        }

        expressPopup.find('img').css('cursor', 'auto');

        $('textarea').on('input', function () {

            const textareaHeight = Math.min(this.scrollHeight + 22.5, 100); // Ensure max height of 100px;
            const counterLength = $(this).val().length;
        
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';

            const inputArea = document.getElementsByClassName('express-input-area')[0];
            if ($(inputArea).hasClass('express-input-area')) {
                darkMode.classList.remove('darkmode-icon2');
            } 
            $(this).closest('.express-input-area').css('height', textareaHeight + 'px');

            // Enable scrollbar when textarea height exceeds 100px
            if (textareaHeight >= 99) {
                $(this).css('overflow-y', 'auto');
            } else {
                $(this).css('overflow-y', 'hidden');
            }


            if ($(this).val().length === 0) {
                if (window.innerWidth >= 1919) {
                    $(this).closest('.express-input-area').css('height', '48px');
                } else {
                    $(this).closest('.express-input-area').css('height', '38px');
                }
            }

            $('.counter').text(counterLength + '/256');
        });

        $('express-input-area').on('input', function () {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        function handleMouseup(e) {
            if (!expressPopup.is(e.target) && expressPopup.has(e.target).length === 0) {
                expressPopup.fadeOut(10, function () {
                    expressButton.insertAfter(expressPopup);
                    $(document).off('mouseup', handleMouseup);
                    $('.darkmode-icon').attr('style','margin-top:30px');
                    if ($(darkMode).hasClass('darkmode-icon2')) {
                        darkMode.classList.remove('darkmode-icon2');
                    }
                });
            }
        }
        $(document).on('mouseup', handleMouseup);
    }); 
    
    
});
