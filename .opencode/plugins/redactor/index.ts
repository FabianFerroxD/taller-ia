// Hook de ejemplo del taller: redacta la palabra SECRETO antes de que el
// prompt llegue al modelo. Se carga solo al iniciar la sesión.

import { Plugin } from "@opencode/plugin"

export default Plugin.define({
  id: "taller.redactor",
  async setup(ctx) {
    await ctx.session.hook("prompt", (event) => {
      event.prompt.text = event.prompt.text.replaceAll("SECRETO", "[redactado]")
    })
  },
})
